# Twitter-X-Scraping

This project is a Python script that uses Selenium to scrape the top 5 trending topics from the Twitter homepage. It logs in to Twitter using your provided credentials and fetches the trending topics from the "What's Happening" section. The script stores the results in a MongoDB database and provides a simple web interface to run the script and view the results.

# Sample 

https://jinit-bhatt.github.io/Twitter-X-Scraping/sample.html

## Features

- Scrapes the top 5 trending topics from the Twitter homepage
- Uses Selenium for web automation and PyMongo for MongoDB interaction
- Employs ProxyMesh service to route each request through a different IP address
- Stores the results in a MongoDB database with a unique ID, trending topics, date and time, and IP address used
- Provides a Flask web interface to run the script and view the results

## Prerequisites

- Python 3.x
- Google Chrome browser
- Chrome WebDriver (compatible with your Chrome version)
- MongoDB installed and running locally
- ProxyMesh account (for rotating proxies)

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/twitter-x-scraper.git
```

2. Install the required Python packages:

```
pip install -r requirements.txt
```

3. Download the Chrome WebDriver for your Chrome version and operating system from the official website: https://sites.google.com/a/chromium.org/chromedriver/downloads

4. Extract the WebDriver executable and add its directory to your system's `PATH` environment variable.

5. Sign up for a ProxyMesh account and obtain your proxy credentials (HTTP and HTTPS proxy URLs).

6. Create a .env file and add

```
TWITTER_USERNAME="Your Username"
TWITTER_PASSWORD="Your Password"
```


## Usage

1. Open the `script.py` file and replace the following placeholders with your credentials:

   - `http://prod-http-proxy.proxymesh.com:31280` and `https://prod-https-proxy.proxymesh.com:31288` with your ProxyMesh HTTP and HTTPS proxy URLs

2. Run the Flask app:

```
python script.py
```

3. Open your web browser and navigate to `http://localhost:5000`.

4. Click the "Run Script" button to fetch the top 5 trending topics from Twitter.

5. The web page will display the trending topics, the date and time of the script execution, the IP address used, and a JSON extract of the record stored in MongoDB.

6. Click the "Run the query again" button to fetch and display the latest trending topics.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

## Acknowledgments

- [Selenium](https://www.selenium.dev/) for web automation
- [PyMongo](https://pymongo.readthedocs.io/) for MongoDB integration
- [Flask](https://flask.palletsprojects.com/) for the web interface
- [ProxyMesh](https://www.proxymesh.com/) for rotating proxy service
#
