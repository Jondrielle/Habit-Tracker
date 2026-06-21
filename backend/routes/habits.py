from fastapi import FastAPI,APIRouter,HTTPException
from schemas.habit import CreateHabit, Habit
from datetime import date 

router = APIRouter()

habits = []

habitID = 0
streak_count = 0

@router.get("/")
async def get_habits():
	return habits

@router.post("/habit", response_model = Habit)
async def create_habit(habit: CreateHabit):
	global habitID

	new_habit = Habit(
		id = habitID,
		name = habit.name,
		description = habit.description,
		is_complete = False,
		streak = 0,
		last_completed = date.today()
	)

	habits.append(new_habit)
	habitID += 1
	return new_habit

@router.delete("/habit/{id}")
async def delete_habit(id: int):
	for habit in habits:
		if habit.id == id:
			habits.remove(habits[id])
		return {"Message:", "Habit Deleted"}

	raise HTTPException(
		status_code = 404,
		detail =  "Habit not found"
	)

@router.patch("/habits/{id}", response_model= Habit)
async def update_habit(id:int):
	for habit in habits:
		if habit.id == id:
			habit.is_complete = not habit.is_complete
			if habit.is_complete:
				habit.streak += 1
				habit.last_completed = date.today()
			return habit

	raise HTTPException(
		status_code = 404,
		detail = "Habit could not be found"
	)

	


