[![Tests](https://github.com/Jondrielle/Habit-Tracker/actions/workflows/tests.yaml/badge.svg)](https://github.com/Jondrielle/Habit-Tracker/actions/workflows/tests.yaml)

# Habit Tracker

A full-stack Habit Tracker application built with **Vue 3** and **FastAPI**. Users can create, edit, delete, and complete habits while tracking daily streaks.

## Features

- Create new habits
- Edit existing habits
- Delete habits
- Mark habits as complete
- Daily streak tracking
- Last completed date tracking
- Responsive card-based layout
- Clean and minimal user interface

## Tech Stack

### Frontend

- Vue 3
- JavaScript
- HTML
- CSS

### Backend

- FastAPI
- Python
- REST API

### Testing & Code Quality

- **GitHub Actions:** Automates testing and code-quality checks when code is pushed to the repository.
- **pytest:** Runs automated tests to verify application functionality.
- **Ruff:** Checks Python code for common errors, style issues, and code-quality improvements.

## Project Structure

```text
Habit-Tracker/
├── frontend/
│   └── Vue application
├── backend/
│   ├── main.py
│   ├── routes/
│   ├── schemas/
│   ├── utils/
│   └── tests/
├── .github/
│   └── workflows/
│       └── tests.yaml
└── requirements.txt
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/Jondrielle/Habit-Tracker.git
cd Habit-Tracker
```

### Backend Setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows, activate it using:

```powershell
venv\Scripts\activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the backend from the `backend` directory:

```bash
cd backend
python -m uvicorn main:app --reload
```

The backend runs at:

http://127.0.0.1:8000

### Frontend Setup

Open a separate terminal from the project root and run:

```bash
cd frontend
npm install
npm run dev
```

The frontend runs at:

http://localhost:5173

## Running Tests

Run the automated tests from the project root:

```bash
python3 -m pytest
```

## Running Code Quality Checks

Check Python code with Ruff from the project root:

```bash
python3 -m ruff check .
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Get all habits |
| POST | `/habit` | Create a habit |
| PATCH | `/habits/{id}` | Update a habit |
| DELETE | `/habit/{id}` | Delete a habit |

## What I Learned

Building this project helped me practice:

- Building REST APIs with FastAPI
- Creating reusable Vue components
- Managing application state
- Implementing CRUD operations
- Connecting frontend and backend using the Fetch API
- Designing responsive user interfaces
- Debugging full-stack applications
- Writing automated tests with pytest
- Using Ruff for Python code-quality checks
- Configuring GitHub Actions for continuous integration

## Known Limitations

This project is a learning exercise focused on understanding CRUD operations using Vue.js and FastAPI. The following limitations remain:

- **In-memory storage:** Habits are stored in a Python list and are lost when the backend restarts.
- **No authentication:** The application does not support user accounts or separate habit lists.
- **Basic error handling:** API errors are primarily logged to the console rather than displayed in the UI.
- **Limited validation:** Form validation and user feedback can be improved.
- **Basic functionality:** The application focuses on core habit management and streak tracking.

## Future Improvements

- Persistent database storage
- User authentication
- Habit completion history
- Categories and tags
- Calendar view
- Improved error handling and form validation
- Additional automated tests and application features

These improvements will be introduced incrementally as I continue developing my skills in Vue.js, FastAPI, REST APIs, and software testing.
