from flask import Flask, render_template

# Configure application
app = Flask(__name__)


# @app.route('/index', methods=['POST', 'GET'])
# #add pages here
# @app.route('/', methods=['POST', 'GET'])                        # home page
# def index():
#
#     greeting = 'Welcome to My Data Science Portfolio Website'
#
#     return render_template('/index.html',
#                             greeting=greeting)


#add pages here
@app.route('/', methods=['POST', 'GET'])                        # home page
def home():

    greeting = 'Welcome to My Portfolio Website'

    return render_template('layout.html',
                            greeting=greeting)


@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():
    return render_template('portfolio.html')


@app.route('/research', methods=['POST', 'GET'])
def research():
    return render_template('research.html')


@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')


@app.route('/npp_distribution', methods=['POST', 'GET'])
def npp_distribution():
    return render_template('npp_dist_test.html')


@app.route('/time_series_prj', methods=['POST', 'GET'])
def time_series_prj():
    return render_template('time_series_prj.html')
