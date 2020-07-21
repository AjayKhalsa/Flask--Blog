from flask import Flask, render_template, url_for
app = Flask(__name__)

# This is where you add routes

posts = [
    {
        'author': 'Ajay Khalsa',
        'title': 'Blog Post 1',
        'content': 'First Post',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Sunny Khalsa',
        'title': 'Blog Post 2',
        'content': 'Second Post',
        'date_posted': 'April 22, 2018'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


# if you add the follying code you can directly run this file in python and won't need to use flask run and set debug environments
if __name__ == '__main__':
    app.run(debug=True)
