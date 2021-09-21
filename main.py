from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from Form import TopicForm
from Scraper import web_request, scrape_data


app = Flask(__name__)
app.config.form_mapping(TESTING=True,SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/')
Bootstrap(app)


@app.route('/', method=['GET','POST'])
def index():
    form = TopicForm(request.form)