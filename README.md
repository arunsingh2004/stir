## Twitter Trending Topics Scraper

This project scrapes the top 5 trending topics from Twitter's "What’s Happening" section using Selenium, stores the data in MongoDB, and displays the results on a webpage.

# Features

Automated scraping of trending topics on Twitter.
Proxy support via ProxyMesh for IP rotation.
Data storage in MongoDB, including metadata (timestamp, unique ID, and IP address).
A simple Flask-based web interface to trigger scraping and display results.
Setup Instructions

1. Clone the Repository
   git clone <https://github.com/arunsingh2004/stir.git>
   cd myenv

2. Set Up Virtual Environment
   python -m venv myenv
   myenv\Scripts\activate

   # For Windows

   source myenv/bin/activate

3. Install Dependencies
   pip install -r requirements.txt

4. Configure ChromeDriver
   Download ChromeDriver from the official website.
   Ensure the ChromeDriver version matches your installed Chrome browser version.
   Place the chromedriver.exe in a directory (e.g., D:\Stir\chromedriver-win64\).
5. Run the Application
   Start the Flask application:

   python app/main.py
   Access the application at http://127.0.0.1:5000/.

6. Trigger Scraping
   Open the webpage.
   Click the button to scrape the latest trending topics.
   View the results directly on the page.
   File Structure

   myenv/
   ├── app/
   │ ├── templates/
   │ │ └── index.html # HTML page for the web interface
   │ ├── selenium_scraper.py # Selenium script for scraping Twitter
   │ ├── database.py # MongoDB connection and storage logic
   │ ├── main.py # Flask app for web interface
   ├── requirements.txt # Dependencies list
   ├── README.md # Project documentation
   Features in Detail

   # Scraping Trending Topics

   Tool: Selenium WebDriver.
   Data Scraped: Top 5 trending topics from Twitter’s "What’s Happening" section.
   Proxy Support: Integrated ProxyMesh for IP rotation.
   Storing Data in MongoDB
   Fields stored in the MongoDB database:

Unique ID for each script run.
Names of the top 5 trends.
Timestamp of the scraping.
IP address used for the request.
Displaying Results
A Flask web application renders the results dynamically.
The web page displays:
Timestamp.
Trending topics.
IP address used for scraping.
JSON representation of the stored data.
Known Issues
Twitter Login Issues: Ensure valid Twitter credentials.
Selector Updates: If Twitter changes its HTML structure, update the XPath selectors in the Selenium script.
ProxyMesh Configuration: Ensure ProxyMesh is correctly set up if using IP rotation.

# Future Enhancements

Support for more platforms like Instagram or LinkedIn.
Pagination and data filtering in the web interface.
Deployment on cloud platforms like AWS or Heroku.
