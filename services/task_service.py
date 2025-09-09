from typing import List, Optional
from storage.task_storage import TaskStorage
from models.task import Task, TaskStatus

class TaskService:
    """Business logic layer for task operations."""
    
    def __init__(self, storage: TaskStorage) -> None:
        self._storage = storage
    
    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """Add a new task."""
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        
        return self._storage.create_task(title.strip(), description.strip() if description else None)
    
    def list_all_tasks(self) -> List[Task]:
        """Get all tasks."""
        return self._storage.get_all_tasks()
    
    def list_pending_tasks(self) -> List[Task]:
        """Get only pending tasks."""
        return self._storage.get_tasks_by_status(TaskStatus.PENDING)
    
    def list_completed_tasks(self) -> List[Task]:
        """Get only completed tasks."""
        return self._storage.get_tasks_by_status(TaskStatus.COMPLETED)
    
    def complete_task(self, task_id: int) -> bool:
        """Mark a task as completed."""
        task = self._storage.get_task(task_id)
        if not task:
            return False
        
        if task.status == TaskStatus.COMPLETED:
            return False  # Already completed
        
        task.mark_completed()
        return True
    
    def uncomplete_task(self, task_id: int) -> bool:
        """Mark a completed task as pending."""
        task = self._storage.get_task(task_id)
        if not task:
            return False
        
        if task.status == TaskStatus.PENDING:
            return False  # Already pending
        
        task.mark_pending()
        return True
    
    def remove_task(self, task_id: int) -> bool:
        """Remove a task by ID."""
        return self._storage.delete_task(task_id)
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a specific task by ID."""
        return self._storage.get_task(task_id)
    
    def update_task(self, task_id: int, title: Optional[str] = None, 
                   description: Optional[str] = None) -> bool:
        """Update task information."""
        if title and not title.strip():
            raise ValueError("Task title cannot be empty")
        
        return self._storage.update_task(
            task_id, 
            title.strip() if title else None, 
            description.strip() if description else None
        )