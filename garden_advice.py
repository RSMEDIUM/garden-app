# Get user input
season = input("Enter the season: ").lower()
plant_type = input("Enter the plant type: ").lower()


def get_season_advice(season):
    """Returns gardening advice based on season"""

    # Season-based logic
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """Returns gardening advice based on plant type"""

    # Plant-type-based logic
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


# Generate combined output
advice = get_season_advice(season) + get_plant_advice(plant_type)

# Output result
print("\nGardening Advice:")
print(advice)