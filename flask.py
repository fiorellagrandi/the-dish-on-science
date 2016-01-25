from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/topic/<team_name>')
def show_team_page(team_name):
    return "Team name: {}".format(team_name)

if __name__ == '__main__':
    app.run(debug=True)
