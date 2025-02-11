from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json

    try:
        parental1 = int(data["parental1"])
        parental2 = int(data["parental2"])
        single_crossover1 = int(data["single_crossover1"])
        single_crossover2 = int(data["single_crossover2"])
        single_crossover3 = int(data["single_crossover3"])
        single_crossover4 = int(data["single_crossover4"])
        double_crossover1 = int(data["double_crossover1"])
        double_crossover2 = int(data["double_crossover2"])

        total_offspring = (
            parental1 + parental2 + single_crossover1 + single_crossover2 +
            single_crossover3 + single_crossover4 + double_crossover1 + double_crossover2
        )

        recombination_AB = (single_crossover1 + single_crossover2 + double_crossover1 + double_crossover2) / total_offspring
        recombination_BC = (single_crossover3 + single_crossover4 + double_crossover1 + double_crossover2) / total_offspring
        recombination_AC = (single_crossover1 + single_crossover2 + single_crossover3 + single_crossover4) / total_offspring

        map_distance_AB = recombination_AB * 100
        map_distance_BC = recombination_BC * 100
        map_distance_AC = recombination_AC * 100

        if map_distance_AC > map_distance_AB and map_distance_AC > map_distance_BC:
            gene_order = "A - B - C"
        elif map_distance_AB > map_distance_AC and map_distance_AB > map_distance_BC:
            gene_order = "B - A - C"
        else:
            gene_order = "A - C - B"

        return jsonify({
            "map_distance_AB": round(map_distance_AB, 2),
            "map_distance_BC": round(map_distance_BC, 2),
            "map_distance_AC": round(map_distance_AC, 2),
            "gene_order": gene_order
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
