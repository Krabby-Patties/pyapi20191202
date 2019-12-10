#!/usr/bin/python3

# allow users to find books via more specific data, such as an entry’s ID.
# Connecting Our API to a Database (SQLite)

import flask
from flask import request, jsonify
import sqlite3
from werkzeug import secure_filename

app = flask.Flask(__name__)
# Starts the debugger. With this line, if your code is malformed, you’ll see an error when you visit your app
app.config["DEBUG"] = True

# assigns function to the attribute row_factory
#converts a row to a dict
def dict_factory(cursor, row):
    d = {}
    # augments the "normal" iteration by the index of the element (it returns tuples (index, element)).
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# decorator page @ 127.0.0.1:5000/
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# Syntax that maps the function to the path /api/v1/resources/books

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()
    # Python dictionaries to the JSON format.
    return jsonify(all_books)


#  create an error page seen by the user if the user encounters an error or inputs a route that hasn’t been defined:
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/books', methods=['GET'])
# Our api_filter function is an improvement on our previous api_id function that returns a book based on its ID. This
# new function allows for filtering by three different fields: id, published, and author.
def api_filter():
    query_parameters = request.args
    # pulls the supported parameters id, published, and author and binds them to appropriate variables:
    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []
    # if [id], [published], or [author] are provided as query parameters, add them to both the query and the
    # filter list:

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()
    # use the jsonify function from Flask to convert our list of results and renders them in the browser as JSON.
    return jsonify(results)


app.run()

if __name__ == '__main__':
    app.run(port=5000)
