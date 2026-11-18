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

/br>
https://deepeval.com/docs/evaluation-end-to-end-single-turn /br>
Single Turn </br>
TurnRelevancyMetric() for Multi-Turn </br>

ConversationalGEval for multiturn,gEval for single turn