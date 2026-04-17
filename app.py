from flask import Flask, render_template, request

app = Flask(__name__)
task = None
movies_list = [
    {
        "title": "Interstellar",
        "rating": 9.5,
        "year": 2014,
        "main_actors": ["Matthew McConaughey", "Anne Hathaway"]
    },
    {
        "title": "Inception",
        "rating": 9.0,
        "year": 2010,
        "main_actors": ["Leonardo Di Caprio", "Joseph Gordon-Levitt"]
    },
    {
        "title": "The Dark Knight",
        "rating": 9.2,
        "year": 2008,
        "main_actors": ["Christian Bale", "Heath Ledger"]
    },
    {
        "title": "Avatar",
        "rating": 8.0,
        "year": 2009,
        "main_actors": ["Sam Worthington", "Zoe Saldana"]
    }
]


@app.route("/")
def index():
    return "Hello, Flask!"


@app.route("/about_me", methods=['GET', 'POST'])
def about_me():
    user = None

    if request.method == 'POST':
        user = {
            "user_name": request.form['name'],
            "age": int(request.form['age']),
            "hobbies": request.form['hobbies'].split(',')
        }

    return render_template("about_me_i.html", user=user)


@app.route('/movies')
def movies_rating():
    return render_template('movie_rate.html', movies=movies_list)


@app.route('/todo', methods=['GET', 'POST'])
def to_do_list():
    global task

    if request.method == 'POST':

        if task:
             task['status'] = request.form['status']
        else:
            task = {
                "task_name": request.form['name'],
                "description": request.form['description'],
                "deadline": request.form['deadline'],
                "status": request.form['status']
            }

    return render_template('todo_list.html', task=task)


app.run(debug=True)
