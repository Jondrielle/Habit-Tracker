# Habit Tracker

A full-stack Habit Tracker application built with **Vue 3** and **FastAPI**. Users can create, edit, delete, and complete habits while tracking daily streaks.

## Features

* Create new habits
* Edit existing habits
* Delete habits
* Mark habits as complete
* Daily streak tracking
* Last completed date tracking
* Responsive card-based layout
* Clean and minimal user interface

## Tech Stack

### Frontend

* Vue 3
* JavaScript
* HTML
* CSS

### Backend

* FastAPI
* Python
* REST API

## Project Structure

```text
frontend/
    Vue application

backend/
    FastAPI application
```

## Installation

### Clone the repository

```bash
git clone https://github.com/Jondrielle/Habit-Tracker.git
cd Habit-Tracker
```

### Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

The backend runs at:

```
http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

The frontend runs at:

```
http://localhost:5173
```

## API Endpoints

| Method | Endpoint       | Description    |
| ------ | -------------- | -------------- |
| GET    | `/`            | Get all habits |
| POST   | `/habit`       | Create a habit |
| PATCH  | `/habits/{id}` | Update a habit |
| DELETE | `/habit/{id}`  | Delete a habit |

## Future Improvements

* Persistent database storage
* User authentication
* Habit completion history
* Categories and tags
* Calendar view
* Mobile optimization

## What I Learned

Building this project helped me practice:

* Building REST APIs with FastAPI
* Creating reusable Vue components
* Managing application state
* CRUD operations
* Frontend and backend communication using the Fetch API
* Responsive UI design
* Debugging full-stack applications

## Screenshots




