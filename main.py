# prints current unix time

import requests
from bs4 import BeautifulSoup
import os
from flask import Flask


def unitime():
	response = requests.get("https://www.unixtimestamp.com/")
	soup = BeautifulSoup(response.content, "html.parser")
	utime = soup.find_all("h3", class_="text-danger")

	return utime[0].getText()

app = Flask(__name__)

@app.route('/unixtime/')
def get_time():
	return unitime()

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 6738))
	app.run(host='0.0.0.0', port=port)