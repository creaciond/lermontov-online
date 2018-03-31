import os.path
from urllib.parse import quote, unquote
from flask import Flask
from flask import render_template, request, redirect, url_for


app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")

# раздел "О проекте"
@app.route("/about_project")
def about_project():
	return render_template("about_project.html")

@app.route("/members")
def members():
	render_template("members.html")

@app.route("/contacts"):
def contacts():
	render_template("contacts.html")

@app.route("/other_projects")
def projects():
	render_template("other_projects.html")

# раздел "Лермонтов"
@app.route("/author")
def author():
	return render_template("author.html")

@app.route("/novel")
def author():
	return render_template("novel.html")

@app.route("/lermontov_language")
def author():
	return render_template("lermontov_language.html")


if __name__ == '__main__':
	app.run()
