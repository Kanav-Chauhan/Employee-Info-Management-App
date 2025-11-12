# 🧑‍💼 Employee Info Management App

A **simple full-stack Django web application** to manage employee records and display **live weather information**.  
Built as part of the **Python Developer assignment** for **Exotica IT Solutions Pvt. Ltd.**

---

## 🚀 Features
- 🧾 **Add, Edit, Delete, and View Employees**
- 🌤 **Fetches live weather data** using the [OpenWeatherMap API](https://openweathermap.org/api)
- 🧠 **Implements Django MVT architecture**
- 💾 Uses **SQLite** for storage
- 🎨 Clean UI built with **Bootstrap**
- 🧩 **Minimal setup – plug and play**

---

## ⚙️ Tech Stack
| Layer | Technology |
|-------|-------------|
| Backend | Python, Django |
| Database | SQLite |
| Frontend | HTML, CSS, Bootstrap |
| API | OpenWeatherMap |
| Optional | Docker for containerized setup |

---


## 🧠 How It Works (MVT Explained)
| Layer | Description |
|--------|-------------|
| **Model** | Defines the Employee data structure (name, email, dept, salary). |
| **View** | Handles logic: CRUD operations + calls the Weather API. |
| **Template** | Displays dynamic data (employee list, weather info) to the user. |

---

## 🌤 Weather API Integration
The app uses **OpenWeatherMap’s Current Weather API** to fetch live weather details for a city (default: Mohali).

---
##  🔧 Setup Instructions

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/employee_project.git
cd employee_project
```
### 2️⃣ Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate # Mac/Linux
```
### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add your OpenWeatherMap API key

```bash
API_KEY = "YOUR_API_KEY"
```

### 5️⃣ Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
### 6️⃣ Start the development server
```bash
python manage.py runserver
```

