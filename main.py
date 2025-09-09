#!/usr/bin/env python3
"""
CLI Task Manager - Main Entry Point

A clean, efficient command-line task management application.
"""

import sys
from storage.task_storage import TaskStorage
from services.task_service import TaskService
from cli.cli_controller import CLIController

def main() -> int:
    """Application entry point."""
    # Initialize the application stack
    storage = TaskStorage()
    service = TaskService(storage)
    controller = CLIController(service)
    
    # Execute the CLI application
    return controller.run()

if __name__ == "__main__":
    sys.exit(main())