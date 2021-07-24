import json
import csv
from json import JSONEncoder
from flask import Flask, jsonify


class User:
    def __init__(self, uid):
        with open('user_details.csv') as datafile:
            entry = csv.reader(datafile)
            for row in entry:
                if uid == row[0]:
                    data = row

        self.name = data[1]
        self.gamename = data[2]
        self.elo = data[3]
        self.played = data[4]
        self.won = data[5]
        self.percent = data[6]


# subclass JSONEncoder
class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


app = Flask(__name__)


@app.route("/<string:username>", methods=['GET'])
def user_details(username: str):
    user = User(username)
    formatteddata = json.dumps(user, indent=4, cls=Encoder)
    return jsonify(formatteddata)


if __name__ == "__main__":
    app.run()
