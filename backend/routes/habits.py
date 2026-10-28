from datetime import date

from fastapi import APIRouter, HTTPException
from schemas.habit import CreateHabit, Habit, UpdateHabit
from utils.streaks import calculate_streak

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
		last_completed = None
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


@router.patch("/habits/{id}", response_model=Habit)
async def update_habit(id: int, updated: UpdateHabit):
    for selected in habits:
        if selected.id == id:
            if updated.name is not None:
                selected.name = updated.name

            if updated.description is not None:
                selected.description = updated.description

            if updated.is_complete is not None:
                if updated.is_complete and not selected.is_complete:
                    today = date.today()

                    selected.streak = calculate_streak(
                        selected.streak,
                        selected.last_completed,
                        today
                    )
                    selected.last_completed = today

                selected.is_complete = updated.is_complete

            return selected

    raise HTTPException(
        status_code=404,
        detail="Habit could not be found"
    )
