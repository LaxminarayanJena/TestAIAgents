import sys
import os
sys.path.insert( 0, os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) ) )



from deepeval.dataset import EvaluationDataset
from deepeval.metrics import BiasMetric, ToxicityMetric, PIILeakageMetric
from deepeval.models import AnthropicModel, DeepEvalBaseEmbeddingModel
from deepeval.synthesizer.config import ContextConstructionConfig
from deepeval.synthesizer.synthesizer import Synthesizer
from deepeval.tracing import observe
from langchain_huggingface import HuggingFaceEmbeddings

from agent_instrumented import support_agent as _support_agent


@observe(name="support_agent")
def support_agent(user_input: str) -> str:
    return _support_agent( user_input )


judge = AnthropicModel(model="claude-haiku-4-5-20251001")
class SentenceTransformerEmbedder(DeepEvalBaseEmbeddingModel):
    def __init__(self):
        self.embedder = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        super().__init__(model="sentence-transformers/all-MiniLM-L6-v2")

    def load_model(self):
        return self.embedder

    def embed_text(self, text: str) -> list[float]:
        return self.model.embed_query(text)

    async def a_embed_text(self, text: str) -> list[float]:
        return self.embed_text(text)

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        return self.model.embed_documents(texts)

    async def a_embed_texts(self, texts: list[str]) -> list[list[float]]:
        return self.embed_texts(texts)

    def get_model_name(self) -> str:
        return self.name


synthesizer = Synthesizer(model=judge)

goldens = synthesizer.generate_goldens_from_docs(
    document_paths=[os.path.join(os.path.dirname(os.path.dirname( os.path.abspath( __file__ ) ) ),"policies.txt")],
    include_expected_output=True,
    max_goldens_per_context=2,
    context_construction_config=ContextConstructionConfig(
        embedder=SentenceTransformerEmbedder(),
        critic_model=judge,
    ),
)

for g in goldens :
    print(g.input)


dataset = EvaluationDataset(goldens =goldens)
biasMetric = BiasMetric(threshold=0.5, model=judge)
toxicMetric = ToxicityMetric(threshold=0.5, model=judge)
personalMetric = PIILeakageMetric(threshold=0.5, model=judge)



for golden in dataset.evals_iterator(metrics=[biasMetric,toxicMetric,personalMetric]):
    support_agent(golden.input)


























