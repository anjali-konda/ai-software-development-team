import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

from agents.requirement_analyst import analyze
from agents.project_manager import plan
from agents.developer import develop
from agents.tester import test
from agents.documentation import document

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze_project():

    requirement = request.form["requirement"]

    requirement_data = analyze(requirement)
    project_data = plan(requirement)
    developer_data = develop(requirement)
    tester_data = test(requirement)
    documentation_data = document(requirement)

    return render_template(
        "result.html",
        requirement=requirement,
        requirement_data=requirement_data,
        project_data=project_data,
        developer_data=developer_data,
        tester_data=tester_data,
        documentation_data=documentation_data
    )


if __name__ == "__main__":
    app.run(debug=True)