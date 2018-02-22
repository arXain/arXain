import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, jsonify
from flask_cors import CORS, cross_origin
from pyXain import pyXain

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py
# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    CORS_HEADER='Content-Type'
))
app.config.from_envvar('NODE_SETTINGS', silent=True)

# Initialize the pyXain manager
pyx = pyXain()
cors = CORS(app, resources={r"/*": {"origins": "*"}})

#max filesize for uploads
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/upload/file', methods=['GET','POST'])
def upload_file():
    results = pyx.upload_paper(request);
    return jsonify(results)

@app.route('/')
def show_index():
    return render_template('index.html')

@app.route('/init/arxain', methods=["GET"])
def init_arxain():
    results = pyx.init_arxain();
    return jsonify(results)

@app.route('/init/author', methods=["GET"])
def init_author():
    author_id = request.args.get('author_id')
    print('/init/author triggered with author_id:')
    print(author_id)

    results = pyx.init_author(author_id)
    return jsonify(results)

@app.route('/submit/manuscript', methods=["GET"])
def submit_manuscript():
    author_id = request.args.get('author_id')
    paper_id = request.args.get('paper_id')
    paper_directory = request.args.get('paper_directory')

    results = pyx.submit_manuscript(author_id, paper_id, paper_directory)

    return jsonify(results)

@app.route('/submit/revision', methods=["GET"])
def submit_revision():
    author_id = request.args.get('author_id')
    paper_id = request.args.get('paper_id')
    paper_directory = request.args.get('paper_directory')

    results = pyx.submit_revision(author_id, paper_id, paper_directory)

    return jsonify(results)

@app.route('/submit/comment', methods=["GET"])
def submit_comment():
    author_id = request.args.get('author_id')
    paper_id = request.args.get('paper_id')
    comment_directory = request.args.get('comment_directory')

    results = pyx.submit_comment(author_id, paper_id, comment_directory)

    return jsonify(results)

@app.route('/pin/manuscript', methods=["GET"])
def pin_manuscript():
    pass
