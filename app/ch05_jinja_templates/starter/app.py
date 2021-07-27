import flask

app = flask.Flask(__name__)

def get_latest_packages():
    return [
        {'name':'flask', 'version':'2.3.1'},
        {'name':'SQL Alchemy', 'version':'1.2.1'},
        {'name':'Bootsrap', 'version':'2.3.4'}
    ]

@app.route('/')
def index():
    test_packages=get_latest_packages()
    return flask.render_template('home/index.html', packages=test_packages)

@app.route('/about')
def about():
    return flask.render_template('home/about.html')

if __name__ == '__main__':
    app.run()