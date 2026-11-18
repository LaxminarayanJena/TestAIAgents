from deepeval.evaluate import evaluate
from deepeval.metrics import TaskCompletionMetric
from deepeval.models import AnthropicModel
from deepeval.test_case import LLMTestCase

from agent_instrumented import support_agent

user_input = "What is the refund policy for electronics?"
actual_output = support_agent(user_input)

test_case = LLMTestCase(
    input=user_input,
    actual_output=actual_output,
)

evaluate(
    test_cases=[test_case],
    metrics=[
        TaskCompletionMetric(
            threshold=0.7,
            model=AnthropicModel(model="claude-sonnet-4-6"),
        )
    ],
)