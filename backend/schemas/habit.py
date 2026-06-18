from pydantic import BaseModel
from typing import Optional 
from datetime import date

class CreateHabit(BaseModel):
	name: str
	description: Optional[str] = None

class Habit(BaseModel):
	id: int
	name: str
	description: Optional[str] = None
	is_complete: bool
	streak: int
	last_completed: Optional[date] = None

