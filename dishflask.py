from flask import Flask, render_template, url_for
from collections import namedtuple
import os
app = Flask(__name__)

TheDish = namedtuple('TheDish', ['official_name', 'subtitle', 'long_name',
                     'blurb', 'description', 'url', 'logo_src'])
thedish = TheDish(official_name='The Dish on Science',
                  subtitle='as told by graduate students',
                  long_name='The Dish on Science: As Told by Graduate Students',
                  blurb='A science blogging club for graduate students.',
                  description='Started by Sam Piekos, The Dish on Science (The Dish for short) offers an avenue for frustrated graduate students to write about the things that they love on the days when those things decide to hate them.',
                  url='http://brunobeltran.org/thedish',
                  logo_src='/images/logo.png')
Author = namedtuple('Author', ['name', 'headshot_src'])
Team = namedtuple('Team', ['url', 'name', 'blurb', 'description', 'logo_src'])

class Post(object):
    """Knows about a blog post for The Dish."""

    def __init__(self, post_directory):
        """ Read JSON into self.__dict__ """
        with open(os.path.join(post_directory, 'post_info.json')) as data_file:
            data = json.loads(data, object_hook=lambda d: namedtuple('Post', d.keys())(*d.values()))
        self.__dict__ = data.__dict__.copy()




@app.route('/topics/<team_name>')
def show_team_page(team_name):
    return "Team name: {}".format(team_name)

@app.route('/science-dictionary/')
def show_dictionary_page():
    return "Dictionary page!"

@app.route('/')
@app.route('/index')
@app.route('/index.htm')
@app.route('/index.html')
@app.route('/home')
def show_home_page():
    return render_template('index.html',


if __name__ == '__main__':
    app.run(debug=True)
