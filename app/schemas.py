from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
import uuid


class IssueStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"


class IssuePriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Issue(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=1000)
    priority: IssuePriority = IssuePriority.MEDIUM
    status: IssueStatus = IssueStatus.OPEN


class IssuePUT(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=1000)
    priority: IssuePriority = IssuePriority.MEDIUM
    status: IssueStatus = IssueStatus.OPEN
