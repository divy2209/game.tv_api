import csv
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/<string:username>", methods=['GET'])
def user_details(username: str):
    with open('user_details.csv') as datafile:
        entry = csv.reader(datafile)
        for row in entry:
            if username == row[0]:
                data = row

    name = data[1]
    gamename = data[2]
    elo = data[3]
    played = data[4]
    won = data[5]
    percent = data[6]

    processed = {'name': name, 'gamename':gamename, 'elo':elo, 'played':played, 'won':won, 'percent':percent}
    return jsonify(**processed)


if __name__ == "__main__":
    app.run()
