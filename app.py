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
        "description": "Cabins, mountain views, hiking, dinner shows, shopping, and family-friendly attractions.",
        "estimated_total_cost": "$600 - $1,200",
        "lodging_cost": "$300 - $700",
        "food_cost": "$150 - $300",
        "activity_cost": "$150 - $250",
        "best_for": "Families, couples, cabins, mountains, weekend getaways",
        "things_to_do": [
            "Visit Great Smoky Mountains National Park",
            "Walk downtown Gatlinburg",
            "Ride the SkyPark chairlift",
            "Visit Ripley’s Aquarium",
            "Book a cabin with mountain views"
        ],
        "budget_tip": "Stay in Pigeon Forge or Sevierville for cheaper lodging and drive into Gatlinburg."
    },
    {
        "name": "Nashville, Tennessee",
        "type": "city",
        "budget": "medium",
        "style": "couple",
        "trip_length": "weekend",
        "max_drive_hours": 4,
        "description": "Live music, restaurants, nightlife, shopping, museums, and a fun weekend atmosphere.",
        "estimated_total_cost": "$700 - $1,400",
        "lodging_cost": "$350 - $800",
        "food_cost": "$200 - $400",
        "activity_cost": "$150 - $300",
        "best_for": "Couples, friends, music lovers, food trips",
        "things_to_do": [
            "Visit Broadway for live music",
            "Tour the Country Music Hall of Fame",
            "Eat hot chicken",
            "Visit the Grand Ole Opry",
            "Explore The Gulch"
        ],
        "budget_tip": "Stay outside downtown and use rideshare when needed to save on hotel costs."
    },
    {
        "name": "New Orleans, Louisiana",
        "type": "city",
        "budget": "medium",
        "style": "couple",
        "trip_length": "weekend",
        "max_drive_hours": 7,
        "description": "Food, music, history, nightlife, riverfront views, and a one-of-a-kind culture.",
        "estimated_total_cost": "$800 - $1,500",
        "lodging_cost": "$350 - $800",
        "food_cost": "$250 - $450",
        "activity_cost": "$150 - $300",
        "best_for": "Couples, friends, food lovers, nightlife",
        "things_to_do": [
            "Walk the French Quarter",
            "Try beignets at Café du Monde",
            "Take a riverboat cruise",
            "Listen to live jazz",
            "Visit Jackson Square"
        ],
        "budget_tip": "Avoid major festival weekends if you want lower hotel prices."
    },
    {
        "name": "Destin, Florida",
        "type": "beach",
        "budget": "medium",
        "style": "family",
        "trip_length": "week",
        "max_drive_hours": 9,
        "description": "White sand beaches, seafood, family fun, clear water, and relaxing beach resorts.",
        "estimated_total_cost": "$900 - $1,800",
        "lodging_cost": "$500 - $1,100",
        "food_cost": "$250 - $450",
        "activity_cost": "$150 - $300",
        "best_for": "Families, beach lovers, relaxing vacations",
        "things_to_do": [
            "Relax at Henderson Beach State Park",
            "Visit HarborWalk Village",
            "Take a dolphin cruise",
            "Book a Crab Island boat tour",
            "Eat seafood on the harbor"
        ],
        "budget_tip": "Look at Fort Walton Beach or Miramar Beach for lower lodging prices."
    },
    {
        "name": "Gulf Shores, Alabama",
        "type": "beach",
        "budget": "medium",
        "style": "family",
        "trip_length": "week",
        "max_drive_hours": 7,
        "description": "Family-friendly beaches, seafood, outdoor activities, and a laid-back coastal feel.",
        "estimated_total_cost": "$800 - $1,500",
        "lodging_cost": "$450 - $900",
        "food_cost": "$200 - $400",
        "activity_cost": "$150 - $250",
        "best_for": "Families, beach trips, budget-friendly coastal vacations",
        "things_to_do": [
            "Spend the day at Gulf State Park",
            "Visit The Wharf",
            "Try fresh seafood",
            "Go mini golfing",
            "Take a dolphin cruise"
        ],
        "budget_tip": "Travel in spring or fall for better rates and smaller crowds."
    },
    {
        "name": "Panama City Beach, Florida",
        "type": "beach",
        "budget": "medium",
        "style": "family",
        "trip_length": "week",
        "max_drive_hours": 8,
        "description": "Beachfront condos, family attractions, restaurants, water activities, and nightlife.",
        "estimated_total_cost": "$850 - $1,700",
        "lodging_cost": "$450 - $1,000",
        "food_cost": "$250 - $450",
        "activity_cost": "$150 - $300",
        "best_for": "Families, friends, beach and entertainment",
        "things_to_do": [
            "Visit Pier Park",
            "Relax on the beach",
            "Take a dolphin tour",
            "Visit St. Andrews State Park",
            "Try beachfront restaurants"
        ],
        "budget_tip": "Book a condo with a kitchen to save money on meals."
    },
    {
        "name": "Orlando, Florida",
        "type": "family",
        "budget": "high",
        "style": "family",
        "trip_length": "week",
        "max_drive_hours": 12,
        "description": "Theme parks, resorts, shopping, restaurants, water parks, and family entertainment.",
        "estimated_total_cost": "$1,800 - $4,500",
        "lodging_cost": "$700 - $1,600",
        "food_cost": "$500 - $1,000",
        "activity_cost": "$600 - $1,900",
        "best_for": "Families, theme parks, kids, entertainment",
        "things_to_do": [
            "Visit Walt Disney World",
            "Visit Universal Orlando",
            "Explore Disney Springs",
            "Spend a day at a water park",
            "Visit ICON Park"
        ],
        "budget_tip": "Stay off-property and choose only one or two park days to control costs."
    },
    {
        "name": "Cancun, Mexico",
        "type": "beach",
        "budget": "high",
        "style": "couple",
        "trip_length": "week",
        "max_drive_hours": 0,
        "description": "All-inclusive resorts, beaches, pools, excursions, nightlife, and tropical relaxation.",
        "estimated_total_cost": "$2,000 - $4,000",
        "lodging_cost": "$1,300 - $2,800",
        "food_cost": "Often included",
        "activity_cost": "$300 - $700",
        "best_for": "Couples, honeymoons, all-inclusive vacations",
        "things_to_do": [
            "Stay at an all-inclusive resort",
            "Visit Isla Mujeres",
            "Take a snorkeling tour",
            "Explore cenotes",
            "Relax on the beach"
        ],
        "budget_tip": "Compare all-inclusive packages because food and drinks can be included."
    },
    {
        "name": "Las Vegas, Nevada",
        "type": "city",
        "budget": "high",
        "style": "friends",
        "trip_length": "weekend",
        "max_drive_hours": 0,
        "description": "Shows, casinos, nightlife, restaurants, pools, shopping, and entertainment.",
        "estimated_total_cost": "$1,200 - $2,800",
        "lodging_cost": "$500 - $1,200",
        "food_cost": "$300 - $700",
        "activity_cost": "$400 - $900",
        "best_for": "Friends, couples, nightlife, entertainment",
        "things_to_do": [
            "Walk the Las Vegas Strip",
            "See a live show",
            "Visit Fremont Street",
            "Try famous restaurants",
            "Relax at a resort pool"
        ],
        "budget_tip": "Visit midweek for cheaper hotel prices."
    },
    {
        "name": "Branson, Missouri",
        "type": "family",
        "budget": "low",
        "style": "family",
        "trip_length": "weekend",
        "max_drive_hours": 5,
        "description": "Shows, lakes, family attractions, shopping, and a budget-friendly weekend getaway.",
        "estimated_total_cost": "$500 - $1,100",
        "lodging_cost": "$250 - $600",
        "food_cost": "$150 - $300",
        "activity_cost": "$100 - $250",
        "best_for": "Families, budget trips, shows, quick getaways",
        "things_to_do": [
            "Visit Silver Dollar City",
            "See a live show",
            "Walk Branson Landing",
            "Visit Table Rock Lake",
            "Try family attractions on the strip"
        ],
        "budget_tip": "Look for show bundles and family attraction passes."
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
        reasons = []

        if destination["trip_length"] == trip_length:
            score += 2
            reasons.append("Matches your trip length")

        if destination["type"] == trip_type:
            score += 3
            reasons.append("Matches your vacation style")

        if destination["budget"] == budget:
            score += 2
            reasons.append("Fits your budget range")

        if destination["style"] == travel_style:
            score += 2
            reasons.append("Good fit for who is traveling")

        if trip_length == "weekend":
            if destination["max_drive_hours"] > 0 and destination["max_drive_hours"] <= drive_hours:
                score += 3
                reasons.append("Fits your preferred driving distance")
            elif destination["max_drive_hours"] == 0:
                score -= 2
            else:
                score -= 3

        if score > 0:
            destination_copy = destination.copy()
            destination_copy["score"] = score
            destination_copy["reasons"] = reasons
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
        favorite_reason=favorite_reason,
        drive_hours=drive_hours
    )


if __name__ == "__main__":
    app.run(debug=True)
