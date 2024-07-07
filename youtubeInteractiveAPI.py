from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

app = Flask(__name__)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)  

driver.get("https://www.youtube.com")

@app.route('/')
def index():
    return 'Flask app is running. Use POST requests to /play, /pause, /rewind, and /forward.'

@app.route('/play', methods=['POST'])
def play():
    try:
        driver.find_element_by_tag_name('body').send_keys('k')
        return jsonify({'status': 'playing'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/pause', methods=['POST'])
def pause():
    try:
        driver.find_element_by_tag_name('body').send_keys('k')
        return jsonify({'status': 'paused'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/rewind', methods=['POST'])
def rewind():
    try:
        for _ in range(10):
            driver.find_element_by_tag_name('body').send_keys(Keys.LEFT)
        return jsonify({'status': 'rewinded'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/forward', methods=['POST'])
def forward():
    try:
        for _ in range(10):
            driver.find_element_by_tag_name('body').send_keys(Keys.RIGHT)
        return jsonify({'status': 'forwarded'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
