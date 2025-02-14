from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# List of reasons why you love Zamila
reasons = [
    "I love how we can talk for hours and never get bored",
    "You have a type of laugh that I've never heard before, I like it :)",
    "Being with you makes me forget everything else",
    "Your eyelashes are pretty",
    "You take up 70% of the bed when we zzz",
    "You almost died in me room",
    "You cry a lot around or with me",
    "You get sad when it's time to leave",
    "You get sOOOooOOooOoOOoO dirty with me heheh",
    "You like talking about our future with me",
    "You make me feel like a baby at times",
    "Sugar momma huehuehuehuehue",
    "You entertain my clingyness",
    "You stay up late at night to talk to me even though you have to study early in the morning",
    "We never need to do anything, you're happy to just be with me",
    "You bot out at times :)",
    "You remember things about me",
    "youregonnahavemebabies",
    "You make silly jokes",
    "You're my favourite distraction (I'm the distraction you're always working like super nerd)",
    "Your nod, the default emote",
    "'But yeah'",
    "'daFuQQq'",
    "'boii whattt'",
    "You make me feel better when I'm upset",
    "You smell nice",
    "You're very positive and nice",
    "You're so comfortable I just wanna go inside you and stay (not like that you dirty baby)",
    "You hate my chicken :( mwah hehe I know you didn't hateeee it",
    "You space out every now and then and you just sit there, it's cute",
    "Your forehead",
    "You watch me lose it at 3am on call",
    "You get in your closet to hide from siblings",
    "Your siblings rely on you :)",
    "You're very family oriented",
    "You don't shame me for anything, you just listen and make me feel better",
    "Your hands are soft and warm, you warm me hands when I'm driving",
    "You're an emotional baby - my emotional baby <3",
    "We can exist together without doing anything",
    "You don't let me mini-nap next to you because 'stopppp there's no timee we only have 9 hours left'",
    "You freak out at cracking noises",
    "You have cute pyjamas (take em off mwah)",
    "You have a small group of friends but I can tell they'll be life-long friends",
]

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)  # This will show the exact error in the browser

@app.route('/get_reason', methods=['GET'])
def get_reason():
    global reasons, original_reasons  # Ensure original_reasons is recognized
    if not reasons:
        reasons = original_reasons.copy()  # Reset the pool when exhausted
    reason = random.choice(reasons)
    reasons.remove(reason)
    return jsonify({"reason": reason})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
