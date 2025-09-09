import argparse
from typing import List

class CommandParser:
    """CLI argument parser with structured command handling."""
    
    def __init__(self) -> None:
        self.parser = self._create_parser()
    
    def _create_parser(self) -> argparse.ArgumentParser:
        """Create the main argument parser with subcommands."""
        parser = argparse.ArgumentParser(
            description="CLI Task Manager - Efficient task management from command line",
            prog="taskman"
        )
        
        subparsers = parser.add_subparsers(dest="command", help="Available commands")
        
        # Add task command
        add_parser = subparsers.add_parser("add", help="Add a new task")
        add_parser.add_argument("title", help="Task title")
        add_parser.add_argument("-d", "--description", help="Task description")
        
        # List tasks command
        list_parser = subparsers.add_parser("list", help="List tasks")
        list_parser.add_argument("-s", "--status", choices=["all", "pending", "completed"], 
                               default="all", help="Filter by task status")
        
        # Complete task command
        complete_parser = subparsers.add_parser("complete", help="Mark task as completed")
        complete_parser.add_argument("id", type=int, help="Task ID")
        
        # Uncomplete task command
        uncomplete_parser = subparsers.add_parser("uncomplete", help="Mark task as pending")
        uncomplete_parser.add_argument("id", type=int, help="Task ID")
        
        # Remove task command
        remove_parser = subparsers.add_parser("remove", help="Remove a task")
        remove_parser.add_argument("id", type=int, help="Task ID")
        
        # Update task command
        update_parser = subparsers.add_parser("update", help="Update task information")
        update_parser.add_argument("id", type=int, help="Task ID")
        update_parser.add_argument("-t", "--title", help="New task title")
        update_parser.add_argument("-d", "--description", help="New task description")
        
        # Show task details command
        show_parser = subparsers.add_parser("show", help="Show task details")
        show_parser.add_argument("id", type=int, help="Task ID")
        
        return parser
    
    def parse_args(self, args: List[str] = None) -> argparse.Namespace:
        """Parse command line arguments."""
        return self.parser.parse_args(args)