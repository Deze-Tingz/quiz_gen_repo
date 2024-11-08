from flask import Flask, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)  # This allows frontend requests

# Load environment variables and configure API
load_dotenv()
api_key = os.environ.get("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable is not set")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/generate-quiz', methods=['GET'])
def generate_quiz():
    response = model.generate_content("Generate a Quiz about Chinese Medicine. A very hard one")
    return jsonify({"quiz": response.text})

if __name__ == '__main__':
    app.run(port=5000)