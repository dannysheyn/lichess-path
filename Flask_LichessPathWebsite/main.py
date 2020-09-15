from flask import Flask, render_template, url_for, request
import pymongo
import myBFS


client = pymongo.MongoClient('mongodb+srv://<username>:<password>@cluster0.pugkn.mongodb.net/test')

app = Flask(__name__)

path_finder = myBFS.FindRouteToMagnus(client, 'LichessDB', 'PlayerGraph')

#
@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def home_page():
    if request.method == 'POST':
        user_name = request.form['UserName']
        path = path_finder.find_path_to_magnus(user_name)
        return render_template('path.html', path=path, header='header.html')
    else:
        return render_template('home.html', header='header.html')


@app.route('/path', methods=['POST', 'GET'])
def path():
    return render_template('path.html', title='Path')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
