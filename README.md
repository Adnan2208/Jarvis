# AI Coding Agent (CLI) in Python

A terminal-based AI coding assistant built from scratch in Python.

The project currently includes:
- A simple CLI chat entry point in [src/main.py](src/main.py)
- Secure file-system helper functions for local tool-style operations:
	- [src/functions/get_files_info.py](src/functions/get_files_info.py)
	- [src/functions/get_files_content.py](src/functions/get_files_content.py)
- A small calculator subproject used for testing and local file operations

## Goals

This project is being developed toward a Claude Code–style terminal agent that can:
- read project files,
- understand user prompts,
- call local helper functions safely,
- and return useful coding assistance directly in the terminal.

## Current Status

### What works now
- CLI prompt input and LLM response generation via Groq in [src/main.py](src/main.py)
- Environment variable loading with `python-dotenv`
- Basic file info listing with directory boundary checks in [src/functions/get_files_info.py](src/functions/get_files_info.py)
- Basic file reading with working-directory boundary checks and max content cap in [src/functions/get_files_content.py](src/functions/get_files_content.py)

### In progress / limitations
- Conversation memory is runtime-only (`messageContextArr` is reset on restart)
- Function-calling/tool orchestration is not yet fully wired into the model loop
- Error handling and truncation messaging can be improved further

## Project Structure

- [src/main.py](src/main.py): CLI entrypoint for model interaction
- [src/functions/get_files_info.py](src/functions/get_files_info.py): list files/directories with metadata
- [src/functions/get_files_content.py](src/functions/get_files_content.py): read file content safely within a working directory
- [src/tests/test_get_files_info.py](src/tests/test_get_files_info.py): manual test script for `get_files_info()`
- [src/tests/test_get_files_content.py](src/tests/test_get_files_content.py): manual test script for `get_files_content()`
- [src/calculator/main.py](src/calculator/main.py): sample calculator CLI app
- [src/calculator/pkg/calculator.py](src/calculator/pkg/calculator.py): calculator logic
- [src/calculator/pkg/render.py](src/calculator/pkg/render.py): JSON output formatting
- [src/calculator/test.py](src/calculator/test.py): unit tests for calculator logic

## Requirements

- Python `>= 3.12`
- Dependencies from [pyproject.toml](pyproject.toml):
	- `groq`
	- `python-dotenv`

## Setup

1. Install dependencies and the package (creates `.venv`):

	 ```
	 uv sync
	 ```

2. Create a `.env` file in the project root with:

	 ```
	 GROQ_API_KEY=your_api_key_here
	 ```

## Usage

Run the CLI agent:

```
uv run Jarvis "Explain how to refactor my parser"
```

Run helper-function test scripts:

```
uv run python src/tests/test_get_files_info.py
uv run python src/tests/test_get_files_content.py
```

Run calculator demo:

```
uv run python src/calculator/main.py "3 * 4 + 5"
```

Run calculator tests:

```
uv run python src/calculator/test.py
```

## Security Notes

The file helper functions are designed to restrict access to the configured working directory using path checks. This is important for building safe terminal agents that should not read arbitrary system files.

## Roadmap

- Persist conversation history across runs
- Add robust tool-calling loop (model decides when to call helper functions)
- Add structured command/response schema for tools
- Improve test coverage and convert manual scripts into formal test suites
- Add richer terminal UX (streaming output, better formatting, command history)

## License

NONE
