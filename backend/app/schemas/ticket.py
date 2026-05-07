from datetime import UTC, datetime
from enum import StrEnum

from sqlmodel import Field, SQLModel


class TicketStatus(StrEnum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    IN_REVIEW = "in_review"
    CLOSED = "closed"


class TicketBase(SQLModel):
    title: str = Field(index=True)
    description: str | None = None
    status: TicketStatus = TicketStatus.OPEN


class Ticket(TicketBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner_id: int = Field(foreign_key="user.id", index=True)
    assigned_id: int | None = Field(foreign_key="user.id", index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class TicketRead(TicketBase):
    id: int
    owner_id: int
    assigned_id: int | None
    created_at: datetime
