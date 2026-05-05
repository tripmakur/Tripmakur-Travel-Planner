from flask import Flask, render_template, request

app = Flask(__name__)

DESTINATIONS = [
    {
        "name": "Gatlinburg, Tennessee",
        "type": "mountain",
        "budget": "low",
        "style": "family",
        "trip_length": "weekend",
        "max_drive_hours": 7,
        "description": "Cabins, hiking, attractions, mountain views, and family-friendly activities."
    },
    {
        "name": "Nashville, Tennessee",
        "type": "city",
        "budget": "medium",
        "style": "couple",
        "trip_length": "weekend",
        "max_drive_hours": 4,
        "description": "Live music, restaurants, nightlife, and a fun quick getaway."
    },
    {
        "name": "New Orleans, Louisiana",
        "type": "city",
        "budget": "medium",
        "style": "couple",
        "trip_length": "weekend",
        "max_drive_hours": 7,
        "description": "Food, music, history, nightlife, and unique culture."
    },
    {
        "name": "Destin, Florida",
        "type": "beach",
        "budget": "medium",
        "style": "family",
        "trip_length": "week",
        "max_drive_hours": 9,
        "description": "White sand beaches, seafood, family fun, and relaxing resorts."
    },
    {
        "name": "Cancun, Mexico",
        "type": "beach",
        "budget": "high",
        "style": "couple",
        "trip_length": "week",
        "max_drive_hours": 0,
        "description": "All-inclusive resorts, beaches, pools, excursions, and nightlife."
    },
    {
        "name": "Orlando, Florida",
        "type": "family",
        "budget": "high",
        "style": "family",
        "trip_length": "week",
        "max_drive_hours": 12,
        "description": "Theme parks, entertainment, resorts, shopping, and family attractions."
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    home_city = request.form.get("home_city")
    trip_length = request.form.get("trip_length")
    trip_type = request.form.get("trip_type")
    budget = request.form.get("budget")
    travel_style = request.form.get("travel_style")
    past_destination = request.form.get("past_destination")
    favorite_destination = request.form.get("favorite_destination")
    favorite_reason = request.form.get("favorite_reason")

    drive_hours = request.form.get("drive_hours")
    drive_hours = int(drive_hours) if drive_hours else 99

    matches = []

    for destination in DESTINATIONS:
        score = 0

        if destination["trip_length"] == trip_length:
            score += 2

        if destination["type"] == trip_type:
            score += 3

        if destination["budget"] == budget:
            score += 2

        if destination["style"] == travel_style:
            score += 2

        if trip_length == "weekend":
            if destination["max_drive_hours"] > 0 and destination["max_drive_hours"] <= drive_hours:
                score += 3
            else:
                score -= 3

        if score > 0:
            destination_copy = destination.copy()
            destination_copy["score"] = score
            matches.append(destination_copy)

    matches = sorted(matches, key=lambda x: x["score"], reverse=True)

    return render_template(
        "results.html",
        matches=matches,
        home_city=home_city,
        trip_length=trip_length,
        trip_type=trip_type,
        budget=budget,
        travel_style=travel_style,
        past_destination=past_destination,
        favorite_destination=favorite_destination,
        favorite_reason=favorite_reason
    )

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True)
