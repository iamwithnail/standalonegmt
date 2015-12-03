__author__ = 'chris'

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/main')
def main_list():
    import exceltojson as etj

    return render_template('grant_list.html', grant_list=etj.build_json())

@app.route('/main/open')
def open_list():
    import exceltojson as etj
    grant_list = []
    return render_template('grant_list.html', grant_list)


if __name__ == '__main__':
    app.debug=True
    app.run()