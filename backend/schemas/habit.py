from datetime import date

from pydantic import BaseModel


class CreateHabit(BaseModel):
	name: str
	description: str | None = None

class Habit(BaseModel):
	id: int
	name: str
	description: str | None = None
	is_complete: bool
	streak: int
	last_completed: date | None = None

class UpdateHabit(BaseModel):
	name: str | None = None
	description: str | None = None
	is_complete: bool | None = None