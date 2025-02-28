from flask import render_template, request
from app import app
import re

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[\W]", password):
        strength += 1
    return strength

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        strength = check_password_strength(password)
        recommendations = []
        if strength < 1:
            recommendations.append("Use at least 8 characters.")
        if not re.search(r"[A-Z]", password):
            recommendations.append("Include uppercase letters.")
        if not re.search(r"[a-z]", password):
            recommendations.append("Include lowercase letters.")
        if not re.search(r"[0-9]", password):
            recommendations.append("Include numbers.")
        if not re.search(r"[\W]", password):
            recommendations.append("Include special characters.")
        return render_template('index.html', strength=strength, recommendations=recommendations, password=password)
    return render_template('index.html', strength=None, recommendations=None, password=None)
