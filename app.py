from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sys
print("Python search path:", sys.path)
from models.postgres_model import fetch_postgres_data
from models.mongo_model import fetch_mongo_data
from services.llm_service import translate_query

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get('query')
    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    try:
        database_query = translate_query(user_query)
        if "SELECT" in database_query.upper():
            result = fetch_postgres_data(database_query)
        else:
            result = fetch_mongo_data(database_query)
        return jsonify({"results": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
