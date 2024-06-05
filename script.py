from dotenv import load_dotenv
import os
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pymongo import MongoClient
from datetime import datetime
import uuid
from flask import Flask, render_template, request
import requests

# Set up MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client['twitter_trends']
collection = db['trends']

# Set up Flask app
app = Flask(__name__)

# Selenium script to fetch Twitter trends
def fetch_twitter_trends():
    proxy = Proxy({
        'proxyType': ProxyType.PAC,
        'proxyAutoconfigUrl': './us-ca.pac'
    })

    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=%s' % proxy.http_proxy)

    driver = webdriver.Chrome(options=chrome_options)


    driver.get("https://x.com/i/flow/login")

    load_dotenv()
    username = os.getenv('TWITTER_USERNAME')
    password = os.getenv('TWITTER_PASSWORD')


    # Log in to Twitter (replace with your own credentials)
    time.sleep(7)
    driver.find_element(By.XPATH, "//input").send_keys(username+ Keys.RETURN)

    time.sleep(7)
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password + Keys.RETURN)
    time.sleep(10)

    #get ip address
    response = requests.get('https://api.ipify.org')
    ip_address = response.text

    # Get What's Happening Topics
    trending_topics = driver.find_elements(By.XPATH,"//div[@aria-label='Timeline: Trending now']//span")
    print(trending_topics)
    top_trends = [trend.text for trend in trending_topics]
    print(top_trends)
    what_happening=[]
    i=0
    while i < len(top_trends)-1:
        if "Trending" in top_trends[i]:
            i+=1
            what_happening.append(top_trends[i])
        i+=1
    print(what_happening)
    if len(what_happening) < 5:
        what_happening.append("No trending topics found")

    # Store results in MongoDB
    unique_id = str(uuid.uuid4())
    data = {
        "_id": unique_id,
        "nameoftrend1": what_happening[0],
        "nameoftrend2": what_happening[1],
        "nameoftrend3": what_happening[2],
        "nameoftrend4": what_happening[3],
        "nameoftrend5": what_happening[4],
        "datetime": datetime.now(),
        "ip_address": ip_address
    }
    collection.insert_one(data)

    # Close the driver
    driver.quit()

    return data

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    data = fetch_twitter_trends()
    return render_template('results.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)