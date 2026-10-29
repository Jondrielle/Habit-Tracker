[![Tests](https://github.com/Jondrielle/Habit-Tracker/actions/workflows/tests.yaml/badge.svg)](https://github.com/Jondrielle/Habit-Tracker/actions/workflows/tests.yaml)

# 📅 Habit Tracker

A full-stack Habit Tracker application built with **Vue 3** and **FastAPI**. Users can create, edit, delete, and complete habits while tracking daily streaks.

## ✨ Features

- ➕ Create new habits
- ✏️ Edit existing habits
- 🗑️ Delete habits
- ✅ Mark habits as complete
- 🔥 Daily streak tracking
- 📆 Last completed date tracking
- 📱 Responsive card-based layout
- 🎨 Clean and minimal user interface

## 🛠️ Tech Stack

### 🎨 Frontend

- Vue 3
- JavaScript
- HTML
- CSS

### ⚙️ Backend

- Python
- FastAPI
- REST API

### 🧪 Testing & Code Quality

- **pytest:** Runs automated tests to verify backend functionality and API behavior.
- **Ruff:** Checks Python code for common errors, style issues, and code-quality improvements.
- **GitHub Actions:** Automatically runs tests and code-quality checks when code is pushed to the repository.

## 📂 Project Structure

```text
Habit-Tracker/
├── frontend/
│   └── Vue application
├── backend/
│   ├── main.py
│   ├── routes/
│   │   └── habits.py
│   ├── schemas/
│   │   └── habit.py
│   ├── utils/
│   │   └── streaks.py
│   └── tests/
│       ├── test_routes.py
│       └── test_streaks.py
├── .github/
│   └── workflows/
│       └── tests.yaml
├── .gitignore
└── requirements.txt
```

## 🚀 Installation

### 📋 Prerequisites

- Python 3.13 or later
- Node.js and npm
- Git

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Jondrielle/Habit-Tracker.git
cd Habit-Tracker
```

### 2️⃣ Backend Setup

Create and activate a Python virtual environment from the project root.

**🍎 macOS / 🐧 Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**🪟 Windows**

```powershell
py -m venv .venv
.venv\Scripts\activate
```

📦 Install the Python dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

▶️ Start the backend from the project root:

```bash
python -m uvicorn backend.main:app --reload
```

The backend runs at:

🌐 http://127.0.0.1:8000

📖 Interactive API documentation:

http://127.0.0.1:8000/docs

### 3️⃣ Frontend Setup

Open a separate terminal from the project root.

📂 Navigate to the frontend directory and install the dependencies:

```bash
cd frontend
npm install
```

▶️ Start the frontend development server:

```bash
npm run dev
```

The frontend runs at:

🌐 http://localhost:5173

## 🧪 Running Tests

This project uses **pytest** to test the FastAPI backend.

Activate the virtual environment and run the following command from the project root:

```bash
python -m pytest
```

The automated tests cover API behavior, including:

- 📝 Creating habits with valid and missing data
- 🔢 Verifying default habit values
- 🗑️ Deleting existing and nonexistent habits
- ✏️ Updating individual habit fields
- 🚦 Checking HTTP status codes and response data
- 🔥 Calculating habit streaks

## 🔍 Running Code Quality Checks

Use Ruff to check Python code for common errors and style issues.

Run the following command from the project root:

```bash
python -m ruff check .
```

## 🤖 Continuous Integration

GitHub Actions automatically runs the project's tests and code-quality checks when code is pushed to the repository.

The workflow installs the Python dependencies, runs Ruff, and executes the pytest test suite.

The status badge at the top of this README displays the workflow's current status.

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Retrieve the application or habit list |
| POST | `/habit` | Create a habit |
| PATCH | `/habits/{id}` | Update a habit |
| DELETE | `/habit/{id}` | Delete a habit |


## 📚 What I Learned

Building this project helped me practice:

- 🏗️ Building REST APIs with FastAPI
- 🧩 Creating reusable Vue components
- 🔄 Managing application state
- 🛠️ Implementing CRUD operations
- 🔗 Connecting the frontend and backend using the Fetch API
- 📱 Designing responsive user interfaces
- 🐛 Debugging full-stack applications
- 🧪 Writing automated tests with pytest
- 🔍 Using Ruff for Python code-quality checks
- 🤖 Configuring GitHub Actions for continuous integration
- 🐍 Managing Python dependencies with a virtual environment

## ⚠️ Known Limitations

This project is a learning exercise focused on understanding CRUD operations using Vue.js and FastAPI. The following limitations remain:

- 💾 **In-memory storage:** Habits are stored in a Python list and are lost when the backend restarts.
- 🔐 **No authentication:** The application does not support user accounts or separate habit lists.
- 🚧 **Basic error handling:** API errors and user feedback can be improved.
- 📝 **Limited validation:** Form validation and error messages can be improved.
- ⚙️ **Basic functionality:** The application focuses on core habit management and streak tracking.

## 🔮 Future Improvements

- 💾 Persistent database storage
- 🔐 User authentication
- 📊 Habit completion history
- 🏷️ Categories and tags
- 🗓️ Calendar view
- 🛠️ Improved error handling and form validation
- 🧪 Additional automated tests and application features

These improvements will be introduced incrementally as I continue developing my skills in Vue.js, FastAPI, REST APIs, and software testing.

---

⭐ **Thanks for checking out Habit Tracker!**

These improvements will be introduced incrementally as I continue developing my skills in Vue.js, FastAPI, REST APIs, and software testing.
