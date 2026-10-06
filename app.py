import os
import requests
from flask import Flask, render_template, request, redirect, session, url_for
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev_fallback_key')

# Hardcoded user credentials
VALID_USERS = {
    'student1': 'pass123',
    'student2': 'pass456',
    'simran': 'simran321',
    'sneha': 'sneha321',
    'shivani': 'shivani321',
    'admin': 'admin123'
}

# Your reCAPTCHA secret key
RECAPTCHA_SECRET_KEY = os.getenv('RECAPTCHA_SECRET_KEY')

def verify_recaptcha(recaptcha_response):
    """Verify reCAPTCHA with Google's servers"""
    data = {
        'secret': RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    try:
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = response.json()
        return result.get('success', False)
    except Exception as e:
        print(f"reCAPTCHA verification error: {e}")
        return False

# Exam configuration for different subjects
EXAMS_CONFIG = {
    'python': {
        'name': 'Python Programming',
        'duration': 15,
        'total_questions': 12,
        'passing_score': 5,
        'template': 'pythonexam.html',
        'correct_answers': {
            'q1': 'Both compiled and interpreted',
            'q2': 'Django',
            'q3': 'Flask',
            'q4': 'All of the above',
            'q5': 'input()',
            'q6': '.py',
            'q7': 'def',
            'q8': 'Unordered key-value pair',
            'q9': 'list',
            'q10': 'Type inferred at runtime',
            'q11': 'Mapping of names to objects',
            'q12': 'tuple'
        }
    },
    'cpp': {
        'name': 'C++ Programming',
        'duration': 15,
        'total_questions': 12,
        'passing_score': 5,
        'template': 'cppexam.html',
        'correct_answers': {
            'q1': '.cpp',
            'q2': 'Both A and B',
            'q3': 'main()',
            'q4': 'repeat-until',
            'q5': 'No problem (modern C++)',
            'q6': '<iostream>',
            'q7': 'Polymorphism',
            'q8': 'Function Overriding',
            'q9': 'break',
            'q10': '%',
            'q11': 'All of the above',
            'q12': 'To indicate successful program execution'
        }
    },
    'java': {
        'name': 'Java Programming',
        'duration': 15,
        'total_questions': 12,
        'passing_score': 5,
        'template': 'Javaexam.html',
        'correct_answers': {
            'q1': 'JIT( Just-In-Time Compiler)',
            'q2': 'System.out.println()',
            'q3': 'package',
            'q4': 'Multiple (with classes)',
            'q5': 'Bytecode',
            'q6': 'java.lang',
            'q7': 'main()',
            'q8': 'Java uses references',
            'q9': 'Both',
            'q10': 'extends',
            'q11': 'Object',
            'q12': 'implements'
        }
    },
    'c': {
        'name': 'C Programming',
        'duration': 15,
        'total_questions': 12,
        'passing_score': 5,
        'template': 'cexam.html',
        'correct_answers': {
            'q1': 'int',
            'q2': ';',
            'q3': 'stdio.h',
            'q4': 'scanf()',
            'q5': 'var_1',
            'q6': 'Depends on compiler',
            'q7': 'include',
            'q8': 'Both',
            'q9': 'Both B and C',
            'q10': 'real',
            'q11': 'All of the above',
            'q12': '0'
        }
    }
}

@app.route('/')
def home():
    """Home page with slider"""
    return render_template('homepage.html')

@app.route('/login')
def login_page():
    """Display login page"""
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    """Handle login authentication with reCAPTCHA"""
    # 1. Verify reCAPTCHA first
    recaptcha_response = request.form.get('g-recaptcha-response')
    if not recaptcha_response:
        return render_template('login.html', error="Please verify the reCAPTCHA")

    if not verify_recaptcha(recaptcha_response):
        return render_template('login.html', error="reCAPTCHA verification failed. Please try again.")

    # 2. Then check username/password
    username = request.form.get('username')
    password = request.form.get('password')

    if username in VALID_USERS and VALID_USERS[username] == password:
        session['username'] = username
        session['logged_in'] = True
        return redirect(url_for('choose_exam'))
    else:
        return render_template('login.html', error="Invalid username or password")

@app.route('/choose-exam')
def choose_exam():
    """Display exam selection page"""
    if not session.get('logged_in'):
        return redirect(url_for('login_page'))

    return render_template('chooseexam.html', username=session.get('username'))

@app.route('/exam/<subject>')
def exam_page(subject):
    """Display exam page based on selected subject"""
    if not session.get('logged_in'):
        return redirect(url_for('login_page'))

    if subject not in EXAMS_CONFIG:
        return redirect(url_for('choose_exam'))

    exam_config = EXAMS_CONFIG[subject]
    session['current_subject'] = subject
    session['exam_start_time'] = datetime.now().timestamp()

    return render_template(exam_config['template'],
                         username=session.get('username'),
                         duration=exam_config['duration'],
                         subject=subject)

@app.route('/submit_exam', methods=['POST'])
def submit_exam():
    """Handle exam submission"""
    if not session.get('logged_in'):
        return redirect(url_for('login_page'))

    subject = session.get('current_subject', 'cpp')
    exam_config = EXAMS_CONFIG.get(subject, EXAMS_CONFIG['cpp'])
    correct_answers = exam_config['correct_answers']
    passing_score = exam_config['passing_score']
    exam_name = exam_config['name']

    # Collect answers
    answers = {}
    for q_num in correct_answers.keys():
        answers[q_num] = request.form.get(q_num, '')

    # Evaluate
    results = {}
    score = 0

    for q_num, correct_answer in correct_answers.items():
        user_answer = answers.get(q_num, '')
        is_correct = (user_answer == correct_answer)
        if is_correct:
            score += 1
        results[q_num] = {
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'is_correct': is_correct
        }

    passed = score >= passing_score

    # ✅ Read username BEFORE clearing session
    username = session.get('username', 'Student')

    # Clear session after exam submission
    session.clear()

    return render_template('result.html',
                         username=username,
                         score=score,
                         total=len(correct_answers),
                         passed=passed,
                         results=results,
                         passing_score=passing_score,
                         exam_name=exam_name,
                         percentage=(score/len(correct_answers))*100)

@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)