from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Shulin'}
    posts = [   # fake array of posts
        {
            'author': {'nickname': 'Li'},
            'body': "彪悍的人生何须BB。"
        },
        {
            'author': {'nickname': 'Zhang'},
            'body': "大家好你是猪嗦。"
        }]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
