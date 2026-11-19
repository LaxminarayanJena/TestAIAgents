# TestAIAgents,ChatBots &  RAG Apps with deepEval using metrics,tracing,Goldens,Safety Evals & G-Eval Custom Metrics
Metrics- answer relvancy,filthfulness, tool correctness </br>
TestCases(Goldens) </br>
Judge LLM </br>
Tracing/Instrumentation -hooks into langchain </br>
test runner- Integration with pytest or standalaone evaluate() methods </br>



Prompt alignment: at least 0.7  </br>
Step efficiency: at least 0.5   </br>
Answer relevance: at least 0.7  </br>

DeepEval is the test framework. It:Runs the test cases.
Captures the agent’s response and trace.
Sends the comparison to Haiku.
Calculates the GEval score.
Passes or fails it against threshold=0.79.
Displays and stores the evaluation result.

</br>
https://deepeval.com/docs/evaluation-end-to-end-single-turn </br>
Single Turn </br>
TurnRelevancyMetric() for Multi-Turn </br>

ConversationalGEval for multiturn,gEval for single turn </br>

RAG stands for Retrieval-Augmented Generation. It means the AI retrieves relevant information first, then uses it to generate an answer.uses semantic search sends 3-5 chunks


### **Core Metric Categories: 1-line explanations**

**RAG Metrics**

- **Answer Relevancy:** Measures how directly the generated answer addresses the user's question.
- **Faithfulness:** Checks whether the answer is supported by the retrieved context and avoids hallucinations.
- **Contextual Precision:** Measures whether relevant retrieved information ranks higher than irrelevant information.
- **Contextual Recall:** Measures how much of the relevant information from the source was successfully retrieved.
- **Contextual Relevancy:** Evaluates whether the retrieved context is relevant to the user's query.
- **RAGAS:** A framework for evaluating RAG pipeline quality using multiple metrics.

**AI Agent Metrics**

- **Plan Quality:** Evaluates whether the agent creates an effective plan to complete the task.
- **Plan Adherence:** Measures whether the agent follows its planned steps.
- **Tool Correctness:** Checks whether the agent selects and uses the correct tools.
- **Argument Correctness:** Evaluates whether the agent passes correct inputs and parameters to tools.
- **Task Completion:** Measures whether the agent successfully achieves the requested objective.
- **Step Efficiency:** Evaluates whether the agent completes tasks using minimal unnecessary steps.
- **Goal Accuracy:** Measures whether the final result matches the user's intended goal.

**Multi-Turn & Conversational Metrics**

- **Knowledge Retention:** Measures whether the agent remembers relevant information from previous conversations.
- **Conversation Completeness:** Checks whether all necessary aspects of the conversation or request are addressed.
- **Turn Relevancy:** Evaluates whether each response is relevant to the current conversational turn.
- **Turn Faithfulness:** Checks whether each response is factually consistent with the available context.
- **Role Adherence:** Measures whether the agent consistently follows its assigned role and instructions.

**Safety, Quality & Output Metrics**

- **Hallucination:** Measures the extent to which the AI generates unsupported or fabricated information.
- **Bias:** Evaluates unfair or prejudiced behavior toward particular groups or viewpoints.
- **Toxicity:** Measures harmful, offensive, abusive, or inappropriate language in outputs.
- **Summarization:** Evaluates the accuracy, completeness, and quality of generated summaries.
- **JSON Correctness:** Checks whether generated JSON follows the required structure and syntax.
- **Prompt Alignment:** Measures whether the AI follows the user's instructions and prompt requirements.

**Custom Metrics**

- **G-Eval:** Uses an LLM to evaluate outputs against custom criteria using a defined scoring framework.
- **Conversational G-Eval:** Uses LLM-based evaluation to assess conversational quality against custom criteria.
- **DAGMetric:** Evaluates outputs through a decision-tree-like structure of evaluation criteria.
- **Jeeval:** Provides custom evaluation logic for assessing AI outputs.
- **Custom Python Metrics:** Allow developers to implement their own deterministic evaluation rules using Python code.

