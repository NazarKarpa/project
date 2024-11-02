from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = [123, 'asda', 1444]
@app.route('/')
def index():
    print(url_for('index'))
    return render_template("index.html", title='gey', menu=menu)



@app.route('/about')
def about():
    return '<h1>0 url</h1>'
@app.route('/profile/<path:username>')
def profile(username):
    return f'gay----> {username}'

# with app.test_request_context():
#     print(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)




