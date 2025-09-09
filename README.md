# CLI Task Manager

A straightforward command-line task manager that does exactly what you need without unnecessary complexity. Built for those who prefer efficiency over flashy features.

## Why This Exists

After trying countless task management apps that either lack functionality or overwhelm with features nobody uses, I built this tool. It's designed around the principle that good software should solve problems efficiently without getting in your way.

## What It Does

- Add tasks with optional descriptions
- View tasks filtered by completion status
- Mark tasks complete or revert them to pending
- Remove tasks you no longer need
- Update task details when requirements change
- Show detailed information for specific tasks

## Quick Start

```bash
python main.py add "Deploy the new API endpoint"
python main.py add "Code review for authentication module" -d "Focus on security vulnerabilities"
python main.py list
python main.py complete 1
python main.py list -s pending
```

## Commands Reference

```bash
# Task creation
python main.py add "Task title" [-d "Optional description"]

# Task viewing
python main.py list [-s all|pending|completed]
python main.py show <task_id>

# Task management  
python main.py complete <task_id>
python main.py uncomplete <task_id>
python main.py remove <task_id>
python main.py update <task_id> [-t "New title"] [-d "New description"]
```

## Architecture

The codebase follows a layered architecture because it scales better than throwing everything into one file:

```
models/     → Task data structure and behavior
storage/    → In-memory data management
services/   → Business logic and validation
cli/        → Command parsing and output formatting
main.py     → Entry point that wires everything together
```

Each layer has a single responsibility. The storage layer can be swapped for file-based or database storage without touching the rest of the code.

## Technical Notes

- Python 3.7+ required (uses dataclasses and type hints)
- Zero external dependencies
- Tasks stored in memory during runtime
- Clean exit codes for scripting integration
- Comprehensive error handling with actionable messages

## Implementation Details

The task model uses an enum for status to prevent invalid states. All operations return success/failure indicators rather than throwing exceptions for expected failures. Command parsing is handled through argparse subcommands for clarity.

Data persistence is intentionally simple - using Python dictionaries with integer keys. This makes the code predictable and easy to debug while remaining fast for reasonable task volumes.

## Future Considerations

The current in-memory storage works well for development and short-term use. For persistence across sessions, the storage layer can be extended to write/read JSON files or connect to a database without changing any other code.

Priority levels, due dates, and categories are obvious extensions that fit naturally into the existing task model structure.
