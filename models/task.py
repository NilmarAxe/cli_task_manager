from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"

@dataclass
class Task:
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    created_at: datetime
    completed_at: Optional[datetime] = None
    
    def mark_completed(self) -> None:
        """Mark task as completed and set completion timestamp."""
        self.status = TaskStatus.COMPLETED
        self.completed_at = datetime.now()
    
    def mark_pending(self) -> None:
        """Mark task as pending and clear completion timestamp."""
        self.status = TaskStatus.PENDING
        self.completed_at = None
    
    def __str__(self) -> str:
        status_symbol = "✓" if self.status == TaskStatus.COMPLETED else "○"
        return f"[{self.id}] {status_symbol} {self.title}"