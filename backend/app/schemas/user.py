from datetime import UTC, datetime

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    email: str = Field(index=True, unique=True)
    full_name: str | None = None


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    is_active: bool = True
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class UserRead(UserBase):
    id: int
    is_active: bool
    created_at: datetime
