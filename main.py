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
	return render_template("members.html")

@app.route("/contacts")
def contacts():
	return render_template("contacts.html")

@app.route("/other_projects")
def projects():
	return render_template("other_projects.html")

# раздел "Лермонтов"
@app.route("/author")
def author():
	return render_template("author.html")

@app.route("/novel")
def novel():
	return render_template("novel.html")

@app.route("/lermontov_language")
def lermontov_language():
	return render_template("lermontov_language.html")

# раздел "Комментарий"
@app.route("/comments_history")
def comments_history():
	return render_template("comments_historic.html")

@app.route("/comments_ling")
def comments_ling():
	return render_template("comments_linguistic.html")

# раздел "Интерактив"
@app.route("/films")
def films():
	return render_template("films.html")

@app.route("/maps")
def maps():
	return render_template("maps.html")

@app.route("/texts")
def texts():
	return render_template("texts.html")

# раздел "Литература"
@app.route("/publications")
def publications():
	return render_template("publications.html")

@app.route("/monographies")
def monographies():
	return render_template("monographies.html")

if __name__ == '__main__':
	app.run()
