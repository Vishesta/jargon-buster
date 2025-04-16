# app.py
from flask import Flask, request, render_template

app = Flask(__name__)

JARGON_DICTIONARY = {
    "API": {
        "meaning": "Application Programming Interface - a set of rules that allow programs to talk to each other.",
        "origin": "Software Engineering",
        "example": "Google Maps API lets developers add maps to their websites."
    },
    "MVP": {
        "meaning": "Minimum Viable Product - the simplest version of a product that can still be released.",
        "origin": "Lean Startup Methodology",
        "example": "Dropbox's early MVP was a video demonstrating how it worked."
    },
    "PA": {
        "meaning": "Payment Aggregator - a service provider that facilitates online payments for merchants.",
        "origin": "Fintech / Payments",
        "example": "Razorpay and Juspay are examples of Payment Aggregators in India."
    },
    "SDK": {
        "meaning": "Software Development Kit - tools that developers use to build applications.",
        "origin": "Software Engineering",
        "example": "Facebook offers an SDK for integrating login in mobile apps."
    },
    "KPI": {
        "meaning": "Key Performance Indicator - a measurable value that shows how effectively a company is achieving business objectives.",
        "origin": "Business Management",
        "example": "Monthly active users is a KPI for many apps."
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    term = ""
    if request.method == "POST":
        term = request.form.get("term", "").upper()
        result = JARGON_DICTIONARY.get(term, {})
    return render_template("index.html", term=term, result=result)

if __name__ == "__main__":
    app.run(debug=True)