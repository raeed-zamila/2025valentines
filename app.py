from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# List of reasons why you love Zamila
reasons = [
    "You make me smile even on my worst days.",
    "Your kindness and warmth inspire me every day.",
    "I love how we can talk for hours and never get bored.",
    "You're my safe place and my greatest adventure.",
    "Your laugh is my favorite sound in the world.",
    "You believe in me even when I don’t believe in myself.",
    "Every moment with you feels like magic.",
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_reason', methods=['GET'])
def get_reason():
    reason = random.choice(reasons)
    return jsonify({"reason": reason})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
