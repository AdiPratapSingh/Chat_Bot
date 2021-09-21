from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from Form import TopicForm
from Scraper import web_request, scrape_data

# $ export FLASK_APP=main    or any other name of this file
# flask run
app = Flask(__name__)
app.config.from_mapping(TESTING=True,SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/')
Bootstrap(app)


@app.route('/', methods=['GET','POST'])
def index():
    form_data = TopicForm(request.form)
    if request.method == 'POST' and form_data.validate_on_submit():
        query = form_data.query.data
        query_result = web_request(query)
        scraped_data = scrape_data(query_result)
        print(scraped_data)
        return render_template('Main.html',form=form_data, result=scraped_data)
    return render_template('Main.html',form=form_data)


if __name__ == '__main__':
    app.run()