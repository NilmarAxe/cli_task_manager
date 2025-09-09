from typing import Dict, List, Optional
from models.task import Task, TaskStatus
from datetime import datetime

class TaskStorage:
    """In-memory storage for tasks using dictionary structure."""
    
    def __init__(self) -> None:
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1
    
    def create_task(self, title: str, description: Optional[str] = None) -> Task:
        """Create a new task and store it."""
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            status=TaskStatus.PENDING,
            created_at=datetime.now()
        )
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by ID."""
        return self._tasks.get(task_id)
    
    def get_all_tasks(self) -> List[Task]:
        """Get all tasks sorted by creation date."""
        return sorted(self._tasks.values(), key=lambda t: t.created_at)
    
    def get_tasks_by_status(self, status: TaskStatus) -> List[Task]:
        """Get tasks filtered by status."""
        return [task for task in self._tasks.values() if task.status == status]
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID. Returns True if successful."""
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
    
    def update_task(self, task_id: int, title: Optional[str] = None, 
                   description: Optional[str] = None) -> bool:
        """Update task properties. Returns True if successful."""
        task = self._tasks.get(task_id)
        if not task:
            return False
        
        if title:
            task.title = title
        if description is not None:
            task.description = description
        return True
    
    def get_task_count(self) -> int:
        """Get total number of tasks."""
        return len(self._tasks)