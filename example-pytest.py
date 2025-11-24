def test_with_single_test_file():
  """Test the agent's basic ability via a session file."""
  AgentEvaluator.evaluate(
    "tests.integration.fixture.home_automation_agent",
    "tests/integration/fixture/home_automation_agent/simple_test.test.json",
  )
