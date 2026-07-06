from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from database import create_database, save_chat
from datetime import datetime

app = Flask(__name__)

create_database()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].lower()

    # Live Time
    if "time" in user_message:
        bot_response = "Current Time: " + datetime.now().strftime("%I:%M %p")

    # Live Date
    elif "date" in user_message:
        bot_response = "Today's Date: " + datetime.now().strftime("%d-%m-%Y")

    else:
        bot_response = get_response(user_message)

    save_chat(user_message, bot_response)

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)