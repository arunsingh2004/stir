from flask import Flask, render_template, jsonify
from selenium_scraper import scrape_trending_topics
from database import store_in_mongodb

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script', methods=['GET'])
def run_script():
    try:
        # Run Selenium script and store results
        trends, ip_address = scrape_trending_topics()
        result = store_in_mongodb(trends, ip_address)
        return jsonify(result)
    except Exception as e:
        print(f"Error occurred: {e}")  # Log the error in the console
        return jsonify({"error": str(e)}), 500  # Return error as JSON for debugging


if __name__ == '__main__':
    app.run(debug=True)
