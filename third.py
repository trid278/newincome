from flask import Flask, request, jsonify
from waitress import serve
import os

app = Flask(__name__)

qa_database = {
    "what is ai": "AI (Artificial Intelligence) refers to the simulation of human intelligence in machines.",
    "what is python": "Python is a high-level programming language known for its simplicity and readability.",
    "who created python": "Python was created by Guido van Rossum and first released in 1991.",
    "what is machine learning": "Machine Learning is a branch of AI that allows computers to learn from data without being explicitly programmed."
}

@app.route('/ask', methods=['GET'])
def ask_question():
    user_question = request.args.get('question', '').lower().strip()
    answer = qa_database.get(user_question, "Sorry, I don't have an answer for that.")
    return jsonify({"question": user_question, "answer": answer})

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Simple Q&A API!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # Default port for local testing
    serve(app, host="0.0.0.0", port=port)
