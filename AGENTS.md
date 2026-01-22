# Repository Guidelines

## Project Structure & Module Organization
- `remarkable_mcp/` holds the core package (API, SSH transport, extraction, tools, resources, prompts).
- `server.py` is the backwards-compatible entry point; `remarkable_mcp/cli.py` is the main CLI.
- `docs/` contains user/developer documentation and assets; `docs/tools.md` mirrors tool behavior.
- `test_server.py` is the primary test suite.
- `pyproject.toml` defines dependencies, tooling, and formatting rules.

## Build, Test, and Development Commands
Use `uv` for dependency management and execution.
- `uv sync --all-extras` — install runtime + dev + optional extras.
- `uv run python server.py` — run the MCP server locally.
- `uv run pytest test_server.py -v` — run the test suite.
- `uv run pytest test_server.py -v --cov=remarkable_mcp` — run tests with coverage.
- `uv run ruff check .` — lint (required by CI).
- `uv run ruff format .` — format (required by CI).

## Coding Style & Naming Conventions
- Python with 4-space indentation; line length is 100.
- Formatting and linting are enforced by `ruff` (`ruff format`, `ruff check`).
- Use `snake_case` for modules/functions and `PascalCase` for classes.
- When adding tools in `remarkable_mcp/tools.py`, follow the XML-structured docstring pattern (`<usecase>`, `<instructions>`, `<parameters>`, `<examples>`).

## Testing Guidelines
- Tests use `pytest` with `pytest-asyncio`; async tests should use `@pytest.mark.asyncio`.
- Place new tests in `test_server.py` or new `test_*.py` files following pytest conventions.
- Prefer focused tests that exercise tools and server behavior (API responses, OCR paths, resource URIs).

## Commit & Pull Request Guidelines
- Commit messages follow Conventional Commits as seen in history (e.g., `feat:`, `fix:`, `ci:`, `build(deps):`, `refactor:`).
- Work on feature branches; `main` is protected and requires a PR.
- PRs should include a clear description, testing performed, and documentation updates when tools change (README table + `docs/tools.md`).

## Security & Configuration Tips
- Do not commit secrets. Use environment variables like `REMARKABLE_TOKEN`, `GOOGLE_VISION_API_KEY`, and `REMARKABLE_SSH_*` locally.
- When testing SSH mode, ensure developer mode is enabled on the device and prefer USB connections for speed.
