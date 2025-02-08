import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
google_gemini_api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

genai.configure(api_key=google_gemini_api_key)
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.form["message"]
    try:
        response = model.generate_content(message)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
