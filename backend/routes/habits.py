from fastapi import FastAPI,APIRouter,HTTPException
from schemas.habit import CreateHabit, Habit, UpdateHabit
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
			habits.remove(habit)
		return {"Message:", "Habit Deleted"}

	raise HTTPException(
		status_code = 404,
		detail =  "Habit not found"
	)

@router.patch("/habits/{id}", response_model= Habit)
async def update_habit(updated:UpdateHabit,id:int):
	for selected in habits:
		if selected.id == id:
			if updated.name is not None:
				selected.name = updated.name
			
			if updated.description is not None:
				selected.description = updated.description

			if updated.is_complete is not None:
				selected.is_complete = updated.is_complete
				if updated.is_complete and selected.last_completed != date.today():
					selected.streak += 1
					selected.last_completed = date.today()
			return selected

	raise HTTPException(
		status_code = 404,
		detail = "Habit could not be found"
	)

	


