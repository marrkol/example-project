from flask import Flask, jsonify,request
import json

app = Flask(__name__)

with open('animations.json', 'r') as file:
    animations = json.load(file)


@app.route('/titles', methods=['GET'])
def get_titles():
    titles = [animation['Original title'] for animation in animations['animations']]
    return jsonify(titles)

@app.route('/directors/<expression>', methods=['GET'])
def get_directors(expression):
    directors = set()
    for animation in animations['animations']:
        if expression.lower() in animation['Directors'].lower():
            directors.update(animation['Directors'].split(', '))
    return jsonify(list(directors))

@app.route('/titles', methods=['GET'])
def get_titles_by_year():
    try:
        from_year = int(request.args.get('from', 0))   # Default to 0 if not provided
        to_year = int(request.args.get('to', 9999))    # Default to 9999 if not provided
    except ValueError:
        return jsonify({"error": "Invalid year format"}), 400

    titles = [
        animation['Original title']
        for animation in ANIMATIONS['animations']  # Assuming ANIMATIONS is a global constant
        if from_year <= int(animation['Year of production']) <= to_year
    ]

    return jsonify(titles)


if __name__ == '__main__':
    app.run(debug=True)
