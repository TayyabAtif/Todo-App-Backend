# FastAPI MongoDB User Authentication API

This is a FastAPI backend application that implements basic **user authentication** using **MongoDB**. The project is organized into folders for maintainability and includes:

- ✅ User **Sign-Up**
- 🔐 User **Login**
- 🛡️ Token-based **Authorization**
- 📁 Modular folder structure using `infrastructure`, `user_controller`, and `task_controller`

---

## 🗂️ Folder Structure

.
├── main.py
├── infrastructure/
│ └── db.py # MongoDB connection
├── user_controller/
│ ├── init.py
│ ├── signup_service.py # User registration logic
│ ├── auth_service.py # Login/token verification logic
│ └── user_routes.py # Signup, login, and protected routes
├── task_controller/
│ └── task_routes.py # Task routes (public)

📬 API Endpoints (Testable via Postman)
🔐 POST /signup
Registers a new user.

Body (x-www-form-urlencoded):

username: john

password: secret123

🔐 POST /login
Logs in and returns a token.

Body (x-www-form-urlencoded):

username: john

password: secret123

🛡️ GET /profile (Protected)
Requires Bearer token.
