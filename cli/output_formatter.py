from typing import List
from models.task import Task
from datetime import datetime

class OutputFormatter:
    """Format output for CLI display with consistent styling."""
    
    @staticmethod
    def format_task_list(tasks: List[Task], title: str = "Tasks") -> str:
        """Format a list of tasks for display."""
        if not tasks:
            return f"{title}: No tasks found."
        
        output = [f"\n{title} ({len(tasks)} total):"]
        output.append("-" * 50)
        
        for task in tasks:
            status_icon = "✓" if task.status.value == "completed" else "○"
            output.append(f"[{task.id:2d}] {status_icon} {task.title}")
            
            if task.description:
                output.append(f"     Description: {task.description}")
        
        return "\n".join(output)
    
    @staticmethod
    def format_task_details(task: Task) -> str:
        """Format detailed task information."""
        lines = [
            f"\nTask Details:",
            f"ID: {task.id}",
            f"Title: {task.title}",
            f"Description: {task.description or 'None'}",
            f"Status: {task.status.value.capitalize()}",
            f"Created: {task.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        ]
        
        if task.completed_at:
            lines.append(f"Completed: {task.completed_at.strftime('%Y-%m-%d %H:%M:%S')}")
        
        return "\n".join(lines)
    
    @staticmethod
    def format_success(message: str) -> str:
        """Format success message."""
        return f"✓ {message}"
    
    @staticmethod
    def format_error(message: str) -> str:
        """Format error message."""
        return f"✗ {message}"
    
    @staticmethod
    def format_info(message: str) -> str:
        """Format informational message."""
        return f"ℹ {message}"