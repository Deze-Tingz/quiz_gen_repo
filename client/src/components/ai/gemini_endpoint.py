from flask import Flask, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
import sys

# Load environment variables and configure API
load_dotenv()
api_key = os.environ.get("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable is not set")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_quiz_content():
    response = model.generate_content("Generate a Quiz about Chinese Medicine. A very hard one")
    return response.text

# Flask app setup
app = Flask(__name__)
CORS(app)

@app.route('/generate-quiz', methods=['GET'])
def generate_quiz():
    quiz = generate_quiz_content()
    return jsonify({"quiz": quiz})

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--terminal':
        # Run in terminal mode
        print("\nGenerating Chinese Medicine Quiz...\n")
        quiz = generate_quiz_content()
        print(quiz)
    else:
        # Run as web server
        app.run(port=5000)