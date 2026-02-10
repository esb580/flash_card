"""Flash card web app. Run with: flask --app app run or python app.py"""
from flask import Flask, render_template, session, redirect, url_for

from config import SECRET_KEY, RUN_HOST, RUN_PORT
from load_topics import load_topics, get_topic

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route("/")
def index():
    """List topics; user picks one to study."""
    topics = load_topics()
    return render_template("index.html", topics=topics)


@app.route("/study/<topic_id>")
def study(topic_id):
    """Show one card from the topic. Session holds current card index."""
    topic = get_topic(topic_id)
    if not topic or not topic["cards"]:
        return redirect(url_for("index"))
    cards = topic["cards"]
    # Initialize or read session for this topic
    if session.get("topic_id") != topic_id:
        session["topic_id"] = topic_id
        session["card_index"] = 0
    idx = session.get("card_index", 0)
    if idx >= len(cards):
        session["card_index"] = 0
        idx = 0
    card = cards[idx]
    return render_template(
        "study.html",
        topic_id=topic_id,
        topic_title=topic["title"],
        card=card,
        card_num=idx + 1,
        total=len(cards),
    )


@app.route("/study/<topic_id>/next")
def next_card(topic_id):
    """Move to next card and redirect to study view."""
    topic = get_topic(topic_id)
    if not topic:
        return redirect(url_for("index"))
    if session.get("topic_id") != topic_id:
        session["topic_id"] = topic_id
        session["card_index"] = 0
    session["card_index"] = session.get("card_index", 0) + 1
    return redirect(url_for("study", topic_id=topic_id))


if __name__ == "__main__":
    app.run(host=RUN_HOST, port=RUN_PORT)
