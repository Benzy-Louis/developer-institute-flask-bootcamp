import flask
from flask import render_template_string

app = flask.Flask(__name__)


@app.route('/')
def index():
    my_template = '''
        <html>
            <head>
                <title>Home Page - Microblog</title>
            </head>
            <body>
                <h1>Hello {{ firstname }} {{ lastname }} says: Wubbalubbadubdub!</h1>
            </body>
        </html>
    '''

    html = render_template_string(
        my_template, firstname="Rick", lastname="Sanchez")
    return html


@app.route('/blog')
def blog():
    my_template = '''
        <html>
            <head>
                <title>Home Page - Microblog</title>
            </head>
            <body>
                <h1>{{ firstname }} {{ lastname }} says: Wubbalubbadubdub!</h1>
            </body>
        </html>
    '''

    html = render_template_string(
        my_template, firstname="Rick", lastname="Sanchez")
    return html


@app.route('/blog/articles')
def articles():
    my_template = '''
        <html>
            <head>
                <title>Home Page - Microblog</title>
            </head>
            <body>
                <h1>{{ firstname }} {{ lastname }} says: Wubbalubbadubdub!</h1>
            </body>
        </html>
    '''

    html = render_template_string(
        "my articles: {{articles}}", firstname="Rick", lastname="Sanchez")
    return html


if __name__ == "__main__":
    app.run(debug=True, port=5000)
