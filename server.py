from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize Flask
app = Flask(__name__)

# Initialize chatbot
chatbot = ChatBot("AI Chatbot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Serve frontend
@app.route("/")
def home():
    return render_template("index.html")

# API route for chatbot
@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json.get("message")
    response = str(chatbot.get_response(user_input))
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

