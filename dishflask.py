from flask import Flask, render_template, url_for, send_from_directory
from collections import namedtuple
import random
import os
import json
from dateutil.parser import parse

app = Flask(__name__, static_url_path='')

TheDish = namedtuple('TheDish', ['official_name', 'subtitle', 'long_name',
                     'blurb', 'description', 'url', 'logo_src'])
thedish = TheDish(official_name='The Dish on Science',
                  subtitle='as told by graduate students',
                  long_name='The Dish on Science: As Told by Graduate Students',
                  blurb='A science blogging club for graduate students.',
                  description='Started by Sam Piekos, The Dish on Science (The Dish for short) offers an avenue for frustrated graduate students to write about the things that they love on the days when those things decide to hate them.',
                  url='http://brunobeltran.org/thedish',
                  logo_src='/images/logo.jpg')
# usused since Author is just a field of post for now
# Author = namedtuple('Author', ['name', 'headshot_src'])

# load all the team information from a global file
Team = namedtuple('Team', ['url', 'name', 'blurb', 'description', 'logo_src'])
team_data = open('/var/www/thedishonscience.com/blog-teams.json').read()
teams = json.loads(team_data, object_hook=lambda d: namedtuple('Team', d.keys())(*d.values())).teams

class Post(object):
    """Knows about a blog post for The Dish."""

    def __init__(self, post_directory):
        """ Read JSON into self.__dict__ """
        post_data = open(os.path.join(post_directory, 'post_info.json')).read()
        data = json.loads(post_data, object_hook=lambda d: namedtuple('Post', d.keys())(*d.values()))
        self.__dict__ = data.__dict__.copy()
        self.publication_date = parse(self.publication_date)
        self.url = '/posts/' + str(self.publication_date.year) + '/' + str(self.url_title)
        self.absolute_url = thedish.url + self.url
        self.teams = [team for team in teams if team.name in self.teams]


# load posts from posts directory
post_directories = os.listdir('/var/www/thedishonscience.com/posts')
recent_posts = [Post(os.path.join('/var/www/thedishonscience.com', 'posts', post_directory)) for post_directory in post_directories]
popular_posts = list(recent_posts)
random.shuffle(popular_posts)


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
    return render_template('index.html', thedish=thedish, teams=teams,
                           popular_posts=popular_posts, recent_posts=recent_posts)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('/var/www/thedishonscience.com/assets', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('/var/www/thedishonscience.com/images', path)


if __name__ == '__main__':
    app.run(debug=True)
