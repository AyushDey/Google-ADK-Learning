# ADK Deployment

ADK's command line interface provides shortcuts to deploy agents to Agent Engine, Cloud Run, and Google Kubernetes Engine (GKE). You can use the following base commands to deploy to each of these services:

- [`adk deploy agent_engine`](https://github.com/google/adk-python/blob/c52f9564330f0c00d82338cc58df28cb22400b6f/src/google/adk/cli/cli_tools_click.py#L1037) (with its command line args described under the `@deploy.command("agent_engine")` decorator)
- [`adk deploy cloud_run`](https://github.com/google/adk-python/blob/c52f9564330f0c00d82338cc58df28cb22400b6f/src/google/adk/cli/cli_tools_click.py#L861) (with its command line args described under the `@deploy.command("cloud_run")` decorator)
- [`adk deploy gke`](https://github.com/google/adk-python/blob/c52f9564330f0c00d82338cc58df28cb22400b6f/src/google/adk/cli/cli_tools_click.py#L1192) (with its command line args described under the `@deploy.command("gke")` decorator)

The `adk deploy agent_engine` command wraps your agent in a [reasoning_engines.AdkApp](https://cloud.google.com/python/docs/reference/vertexai/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp) class and deploys this app to Agent Engine's managed runtime, ready to receive agentic queries.

When an `AdkApp` is deployed to Agent Engine, it automatically uses a [`VertexAiSessionService`](https://google.github.io/adk-docs/sessions/session/#sessionservice-implementations) for persistent, managed session state. This provides multi-turn conversational memory without any additional configuration. For local testing, the application defaults to a temporary, `InMemorySessionService`.
