from flask import Flask
import utils

app = Flask(__name__)

@app.route("/")
def index():
    candidates = utils.get_candidates_all()
    result = "<br>"
    for candidate in candidates:
        result += candidate['name'] + "<br>"
        result += candidate['position'] + "<br>"
        result += candidate['skills'] + "<br>"
        result += "<br>"

    return f"<pre> {result} </pre>"

@app.route("/candidates/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_candidates_by_pk(pk)
    result = "<br>"
    result += candidate['name'] + "<br>"
    result += candidate['position'] + "<br>"
    result += candidate['skills'] + "<br>"
    result += "<br>"
    return f"""
        <img src=="{candidate['picture']}">
        <pre> {result} </pre>
    """

@app.route("/candidates/<skill_name>")
def get_candidate_by_skills(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name.lower())
    result = "<br>"
    for candidate in candidates:
        result += candidate['name'] + "<br>"
        result += candidate['position'] + "<br>"
        result += candidate['skills'] + "<br>"
        result += "<br>"

    return f"<pre> {result} </pre>"

app.run(debug=True)



