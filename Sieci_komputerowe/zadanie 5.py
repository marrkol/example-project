from flask import Flask, jsonify,request
import json

app = Flask(__name__)

with open('animations.json', 'r') as file:
    animations = json.load(file)

@app.route("/")
def hello():
    return "<h1>Hello world!</h1>"

@app.route('/directors/<expression>', methods=['GET'])
def get_directors(expression):
    directors = set()
    for animation in animations['animations']:
        if expression.lower() in animation['Directors'].lower():
            directors.update(animation['Directors'].split(', '))
    return jsonify(list(directors))

@app.route('/titles', methods=['GET'])
def get_titles_by_year():
    if 'from' in request.args and 'to' in request.args:
        from_year = int(request.args.get('from'))
        to_year = int(request.args.get('to'))


        titles = [
            animation['Original title']
            for animation in animations['animations']
            if from_year <= int(animation['Year of production']) <= to_year
        ]

        return jsonify(titles)
    else:
        titles = [animation['Original title'] for animation in animations['animations']]
        return jsonify(titles)


if __name__ == '__main__':
    app.run(debug=True)
