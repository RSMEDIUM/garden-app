def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def generate_advice(season, plant_type):
    advice = ""
    advice += get_season_advice(season)
    advice += get_plant_advice(plant_type)
    return advice


# Hardcoded values still fine for THIS issue
season = "summer"
plant_type = "flower"

print(generate_advice(season, plant_type))