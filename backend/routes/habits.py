from fastapi import FastAPI,APIRouter
from schemas.habit import CreateHabit, ResponseHabit

router = APIRouter()

habits = []

HabitID = 0

@router.get("/habits")
async def get_habits():
	return habits

@router.post("/habit", response_model=ResponseHabit)
async def create_habit(habit: CreateHabit):
	newHabit = ResponseHabit(
		id = habitID,
		name = name,
		description = description,
		is_Complete = False,
		streak = habit.streak,
		last_Completed = habit.last_Completed
	)
	habits.append(newHabit)
	HabitID += 1
	return {"Message": "Habit Created"}




