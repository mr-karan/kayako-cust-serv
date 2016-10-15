import sys
import json
import pprint
import argparse

from flask import Flask, make_response, render_template, jsonify, send_from_directory,request

from twitter import get_tweets

app = Flask(__name__)

@app.route('/')
def index():
    s = get_tweets()
    return render_template('index.html',tweets = s)


@app.route('/fetch')
def more():
    max_id = request.args.get('max_id')
    print("Max ID: "+str(max_id))
    return jsonify(tweets = get_tweets(max_id))


def main():
    app.run(host="0.0.0.0", port=8080, debug=True)
if __name__ == '__main__':
    sys.exit(main())
