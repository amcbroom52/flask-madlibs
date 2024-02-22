from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
def index():
    """Loads root page with prompts from a Story instance."""

    return render_template('questions.html', prompts=silly_story.prompts)


@app.get('/results')
def show_results():
    """Accepts user input as a query string for each prompt. Then creates and
    displays mad lib story utilizing the template from the Story instance
    and user's answers."""

    result_text = silly_story.get_result_text(request.args)

    return render_template('results.html', story=result_text)
