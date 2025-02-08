from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import google.generativeai as genai

app = Flask(__name__)

load_dotenv()
gemini_api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-pro')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        try:
            response = model.generate_content(user_input)
            gemini_response = response.text
        except Exception as e:
            gemini_response = f"Error: {str(e)}"
        return render_template("index.html", gemini_response=gemini_response, user_input=user_input)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
