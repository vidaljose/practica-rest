from flask import Flask, jsonify

app = Flask(__name__)

frameworks = [
    {
        "id":1,
        "name":"flask"
        },
    {
        "id":2,
        "name":"ExpressJS"
        },
    {
        "id":3,
        "name":"Laravel"
        }
    ]

@app.route("/")
def index():
    return "Hola mundo"

@app.route("/api/frameworks/",methods=["GET"])
def get_framework():
    return jsonify(frameworks)

@app.route("/api/frameworks/<string:name>")
def get_framework_by_name(name):
    framework = []
    for f in frameworks:
        if f["name"] == name:
            framework.append(f)
    return jsonify(framework[0])

@app.route("/api/frameworks/<int:id>")
def get_framework_by_id(id):
    framework = []
    for f in frameworks:
        if f["id"] == id:
            framework.append(f)
    return jsonify(framework[0])



if __name__ == "__main__":
    app.run(debug=True)

