import sys
from flask import Flask, render_template, jsonify, request

from twitter import TwitterAPI

app = Flask(__name__)

# Instantiate ``api`` object to setup authentication for Twitter API.
api = TwitterAPI()

@app.route('/')
def index():
    tweets = api.fetch_tweets(max_id=-1)
    return render_template('index.html',tweets = tweets)

@app.route('/load')
def load():
    # Get the lowest tweet id on that page from AJAX request.
    max_id = request.args.get('max_id')
    return jsonify(tweets = api.fetch_tweets(max_id))


def main():
    app.run(host="0.0.0.0", port=8000, debug=True)


if __name__ == '__main__':
    sys.exit(main())
