from flask import Flask, render_template, request

app = Flask(__name__)

DESTINATIONS = [
    {
        "name": "Gatlinburg, Tennessee",
        "type": "Mountains / Road Trip",
        "budget": "low",
        "vibe": ["relaxing", "adventure", "family"],
        "climate": "mountains",
        "why": "Great for cabins, scenic drives, hiking, family attractions, and an affordable driveable getaway.",
        "best_for": "Families, couples, weekend trips",
        "estimated_cost": "$600 - $1,500",
    },
    {
        "name": "Destin, Florida",
        "type": "Beach",
        "budget": "medium",
        "vibe": ["relaxing", "family", "romantic"],
        "climate": "beach",
        "why": "Beautiful beaches, seafood, shopping, and activities for families or couples.",
        "best_for": "Beach vacations, families, couples",
        "estimated_cost": "$1,200 - $3,000",
    },
    {
        "name": "New Orleans, Louisiana",
        "type": "City / Food / Culture",
        "budget": "medium",
        "vibe": ["food", "nightlife", "culture"],
        "climate": "city",
        "why": "Perfect for food, music, history, nightlife, and a unique cultural experience.",
        "best_for": "Couples, friends, food lovers",
        "estimated_cost": "$900 - $2,500",
    },
    {
        "name": "Orlando, Florida",
        "type": "Theme Parks / Family",
        "budget": "high",
        "vibe": ["family", "adventure", "entertainment"],
        "climate": "themeparks",
        "why": "Theme parks, resorts, family entertainment, and plenty of vacation packages.",
        "best_for": "Families and entertainment trips",
        "estimated_cost": "$2,000 - $6,000+",
    },
    {
        "name": "Cancun, Mexico",
        "type": "All Inclusive",
        "budget": "medium",
        "vibe": ["relaxing", "romantic", "beach"],
        "climate": "allinclusive",
        "why": "A strong pick for resorts, beaches, food included, and simple package-style planning.",
        "best_for": "Couples, honeymoons, relaxing trips",
        "estimated_cost": "$1,800 - $4,500",
    },
    {
        "name": "Caribbean Cruise",
        "type": "Cruise",
        "budget": "medium",
        "vibe": ["relaxing", "family", "entertainment"],
        "climate": "cruise",
        "why": "Cruises make planning simple with lodging, meals, entertainment, and multiple stops bundled together.",
        "best_for": "First-time travelers, families, couples",
        "estimated_cost": "$1,500 - $4,000",
    },
]


def score_destination(destination, answers):
    score = 0

    if destination["budget"] == answers.get("budget"):
        score += 3
    elif answers.get("budget") == "high":
        score += 1

    if destination["climate"] == answers.get("vacation_type"):
        score += 4

    interests = answers.getlist("interests")
    for interest in interests:
        if interest in destination["vibe"]:
            score += 2

    if answers.get("travel_group") in destination["vibe"]:
        score += 2

    return score


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/planner")
def planner():
    return render_template("planner.html")


@app.route("/results", methods=["POST"])
def results():
    answers = request.form
    ranked = sorted(
        DESTINATIONS,
        key=lambda destination: score_destination(destination, answers),
        reverse=True,
    )
    top_results = ranked[:3]
    return render_template("results.html", results=top_results, answers=answers)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
