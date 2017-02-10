import sqlite3
import time

from flask import Flask, g, request, render_template, redirect


app = Flask(__name__)
DATABASE = 'twitterish.db'


@app.route("/")
def hello():
    tweets = db_read_tweets()
    print(tweets)
    return render_template('index.html', tweets=tweets)


@app.route("/api/tweet", methods=["POST"])
def receive_tweet():
    print(request.form)
    db_add_tweet(request.form['name'], request.form['tweet'])
    return redirect("/")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def db_read_tweets():
    c = get_db().cursor()
    c.execute("SELECT * FROM twitterish")
    return c.fetchall()


def db_add_tweet(name, tweet):
    c = get_db().cursor()
    t = str(time.time())
    tweet_info = (name, t, tweet)
    c.execute("INSERT INTO twitterish VALUES (?, ?, ?)", tweet_info)
    get_db().commit()


if __name__ == "__main__":
    app.run(debug=True)
