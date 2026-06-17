from pydantic import BaseModel
from typing import Optional 
from datetime import date

def CreateHabit(BaseModel):
	name: str
	description: Optional(str) = None

def ResponseHabit(BaseModel):
	id: int
	name: str
	description: Optional(str) = None
	is_Complete: bool
	streak: int
	last_completed: Optional(date) = None

