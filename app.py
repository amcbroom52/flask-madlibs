from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import story_list

selected_story = {}

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
def index():
    return render_template('index.html', stories=story_list)


@app.get('/prompt')
def get_prompts():
    """Loads root page with prompts from a Story instance."""

    story_name = request.args['stories']

    global selected_story

    for story in story_list:
        if story_name == story.name:
            selected_story = story

    return render_template('questions.html', prompts=selected_story.prompts)


@app.get('/results')
def show_results():
    """Accepts user input as a query string for each prompt. Then creates and
    displays mad lib story utilizing the template from the Story instance
    and user's answers."""

    result_text = selected_story.get_result_text(request.args)

    return render_template('results.html', story=result_text)
