import sys
from typing import Optional
from services.task_service import TaskService
from cli.command_parser import CommandParser
from cli.output_formatter import OutputFormatter

class CLIController:
    """Main CLI controller that coordinates all operations."""
    
    def __init__(self, task_service: TaskService) -> None:
        self._task_service = task_service
        self._parser = CommandParser()
        self._formatter = OutputFormatter()
    
    def run(self, args: Optional[list] = None) -> int:
        """Run the CLI application. Returns exit code."""
        try:
            parsed_args = self._parser.parse_args(args)
            
            if not parsed_args.command:
                self._parser.parser.print_help()
                return 1
            
            return self._execute_command(parsed_args)
        
        except Exception as e:
            print(self._formatter.format_error(f"Unexpected error: {str(e)}"))
            return 1
    
    def _execute_command(self, args) -> int:
        """Execute the appropriate command based on parsed arguments."""
        command_map = {
            "add": self._handle_add,
            "list": self._handle_list,
            "complete": self._handle_complete,
            "uncomplete": self._handle_uncomplete,
            "remove": self._handle_remove,
            "update": self._handle_update,
            "show": self._handle_show
        }
        
        handler = command_map.get(args.command)
        if not handler:
            print(self._formatter.format_error(f"Unknown command: {args.command}"))
            return 1
        
        return handler(args)
    
    def _handle_add(self, args) -> int:
        """Handle add task command."""
        try:
            task = self._task_service.add_task(args.title, args.description)
            print(self._formatter.format_success(f"Task created: [{task.id}] {task.title}"))
            return 0
        except ValueError as e:
            print(self._formatter.format_error(str(e)))
            return 1
    
    def _handle_list(self, args) -> int:
        """Handle list tasks command."""
        if args.status == "pending":
            tasks = self._task_service.list_pending_tasks()
            title = "Pending Tasks"
        elif args.status == "completed":
            tasks = self._task_service.list_completed_tasks()
            title = "Completed Tasks"
        else:
            tasks = self._task_service.list_all_tasks()
            title = "All Tasks"
        
        print(self._formatter.format_task_list(tasks, title))
        return 0
    
    def _handle_complete(self, args) -> int:
        """Handle complete task command."""
        if self._task_service.complete_task(args.id):
            print(self._formatter.format_success(f"Task {args.id} marked as completed"))
            return 0
        else:
            print(self._formatter.format_error(f"Could not complete task {args.id} (not found or already completed)"))
            return 1
    
    def _handle_uncomplete(self, args) -> int:
        """Handle uncomplete task command."""
        if self._task_service.uncomplete_task(args.id):
            print(self._formatter.format_success(f"Task {args.id} marked as pending"))
            return 0
        else:
            print(self._formatter.format_error(f"Could not uncomplete task {args.id} (not found or already pending)"))
            return 1
    
    def _handle_remove(self, args) -> int:
        """Handle remove task command."""
        if self._task_service.remove_task(args.id):
            print(self._formatter.format_success(f"Task {args.id} removed"))
            return 0
        else:
            print(self._formatter.format_error(f"Task {args.id} not found"))
            return 1
    
    def _handle_update(self, args) -> int:
        """Handle update task command."""
        if not args.title and not args.description:
            print(self._formatter.format_error("At least one field (title or description) must be provided"))
            return 1
        
        try:
            if self._task_service.update_task(args.id, args.title, args.description):
                print(self._formatter.format_success(f"Task {args.id} updated"))
                return 0
            else:
                print(self._formatter.format_error(f"Task {args.id} not found"))
                return 1
        except ValueError as e:
            print(self._formatter.format_error(str(e)))
            return 1
    
    def _handle_show(self, args) -> int:
        """Handle show task details command."""
        task = self._task_service.get_task(args.id)
        if task:
            print(self._formatter.format_task_details(task))
            return 0
        else:
            print(self._formatter.format_error(f"Task {args.id} not found"))
            return 1