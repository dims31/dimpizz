from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_pizza_dough(
    total_weight: float,
    hydration: float,
    salt_percent: float,
    olive_percent: float,
    type_levure: str = "fresh",
    duree_totale: float = 24,
) -> dict:
    """Calcule les ingrédients de la pâte à pizza incluant la levure"""
    h = ((hydration) / 100.0 - (olive_percent) / 100.0)
    s = salt_percent / 100.0
    o = olive_percent / 100.0

    flour = total_weight / (1.0 + h + s + o)
    water = flour * h
    salt = flour * s
    olive = flour * o

    # Calcul de la levure
    if type_levure == "fresh":
        ratio_levure = 1
    elif type_levure == "dry":
        ratio_levure = 0.40
    else:
        raise ValueError("type de levure inconnu")
    
    duree_frigo = duree_totale - 4
    yeast_per_kg = ratio_levure *  48 / duree_frigo
    yeast = yeast_per_kg * flour / 1000

    return {
        "flour": round(flour, 0),
        "water": round(water, 0),
        "salt": round(salt, 0),
        "olive": round(olive, 0),
        "yeast": round(yeast, 2),
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    try:
        num_balls = int(data["num_balls"] or 4)
        ball_weight = float(data["ball_weight"] or 260)
        total_weight = num_balls * ball_weight
        hydration = float(data["hydration"])
        salt_percent = float(data["salt_percent"] or 2.5)
        olive_percent = float(data["olive_percent"] or 2.5)
        duree_totale = float(data.get("fermentation_duration", 24))
        type_levure = data.get("yeast_type", "fresh")

        dough = calculate_pizza_dough(
            total_weight=total_weight,
            hydration=hydration,
            salt_percent=salt_percent,
            olive_percent=olive_percent,
            type_levure=type_levure,
            duree_totale=duree_totale,
        )

        return jsonify({
            "success": True,
            "num_balls": num_balls,
            "ball_weight": ball_weight,
            "total_weight": total_weight,
            "dough": dough,
        })

    except (ValueError, KeyError, ZeroDivisionError) as e:
        return jsonify({"success": False, "error": "Saisie invalide"}), 400

if __name__ == "__main__":
    app.run(debug=True)