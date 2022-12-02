import flask

app = flask.Flask(__name__)

articles = [
	{
		"title": "article1",
		"author": "author1",
		"content": "some article1 content"
	},
	{
		"title": "article2",
		"author": "author2",
		"content": "some article2 content"
	}

]


@app.route('/')
def hellow_index():
	return flask.render_template('index.html')


@app.route('/blog')
def wellcome_users():
	return flask.render_template("homepage.html")


@app.route('/blog/articles')
def diaplay_artcles():
	return flask.render_template('articles.html', articles=articles)


if __name__ == "__main__":
	app.run(debug=True, port=8080)
