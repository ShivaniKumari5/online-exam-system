# 📚 Online Examination System

A complete web-based online examination platform built with **Python Flask**.  
Supports multiple programming subjects, timed exams, reCAPTCHA security, and instant results.

## 🎯 Features

- **Secure Login** with Google reCAPTCHA v2
- **4 Programming Subjects** — Python, C++, Java, C
- **Timed Exams** — 15 minutes with 12 questions each
- **Auto-Submit** — Exam automatically submits when time expires
- **Instant Results** — Score, percentage, pass/fail status, question-wise analysis
- **Responsive Design** — Works on mobile, tablet, and desktop

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python Flask | Backend framework |
| HTML / CSS / JS | Frontend interface |
| Google reCAPTCHA v2 | Bot prevention |
| Jinja2 | Templating engine |
| python-dotenv | Environment variable management |

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher
- Internet connection (for reCAPTCHA)

### Step 1: Clone the repository

```bash
git clone https://github.com/ShivaniKumari5/online-exam-system.git
cd online-exam-system
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set up environment variables

Create a `.env` file in the root directory with the following content:

```
RECAPTCHA_SECRET_KEY=your_recaptcha_secret_key
FLASK_SECRET_KEY=your_flask_secret_key
```

Get your reCAPTCHA keys from https://www.google.com/recaptcha/admin

### Step 4: Run the application

```bash
python app.py
```

### Step 5: Open in browser

```
http://127.0.0.1:5000
```

## 🔐 Login Credentials (For Testing)

| Username | Password  |
|----------|-----------|
| student1 | pass123   |
| student2 | pass456   |
| simran   | simran321 |
| sneha    | sneha321  |
| shivani  | shivani321|
| admin    | admin123  |

⚠️ Complete the reCAPTCHA verification before clicking Login.

## 📋 How to Use

1. **Login** — Enter username/password and solve the reCAPTCHA
2. **Select Subject** — Choose from Python, C++, Java, or C
3. **Take Exam** — Answer 12 questions within the time limit
4. **Submit** — Click submit or let the timer auto-submit
5. **View Results** — See score, percentage, and correct/incorrect answers

## 📁 Project Structure

```
online-exam-system/
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not uploaded to Git)
├── .gitignore           # Git ignore rules
├── index.js             # Frontend JavaScript
├── readme.md            # Project documentation
├── templates/           # HTML templates
│   ├── homepage.html
│   ├── login.html
│   ├── chooseexam.html
│   ├── pythonexam.html
│   ├── cppexam.html
│   ├── Javaexam.html
│   ├── cexam.html
│   └── result.html
└── static/              # CSS, JS, and images
    ├── style.css
    └── images/
```

## ⏱️ Exam Details

| Subject | Questions | Duration   | Passing Score |
|---------|-----------|------------|---------------|
| Python  | 12        | 15 minutes | 5 / 12        |
| C++     | 12        | 15 minutes | 5 / 12        |
| Java    | 12        | 15 minutes | 5 / 12        |
| C       | 12        | 15 minutes | 5 / 12        |

## 🔒 Security Features

- Google reCAPTCHA v2 verification on login
- Session-based authentication
- Auto-submit exam on timer expiry
- Sensitive keys stored in `.env` (not committed to Git)
- Prevents back-navigation during exam

## 🔄 How reCAPTCHA Works

```
User opens Login Page
         ↓
Google loads reCAPTCHA widget
         ↓
User clicks "I'm not a robot" checkbox
         ↓
Google gives a response token (long string)
         ↓
User submits login form (username + password + token)
         ↓
Flask receives the token
         ↓
Flask sends token to Google's server for verification
         ↓
Google responds: { success: true } or { success: false }
         ↓
If success → Flask checks username/password
If fail    → Flask shows error message
```

## 📝 Future Enhancements

- Database integration (MySQL / PostgreSQL)
- Admin panel for managing questions and users
- Student registration system
- Detailed analytics and reports
- More subjects and difficulty levels

## 👨‍💻 Author

A personal learning project — built to practice Flask, session management, and reCAPTCHA integration.

## 📄 License

This project is open for learning purposes. Feel free to fork and modify.