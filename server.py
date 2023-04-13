from flask import Flask, render_template, redirect, request
app = Flask(__name__)
app.secret_key = "Valaar Dohaeris"


@app.route('/')
def index():
    return render_template('index.html')

# MORE ROUTES HERE


@app.route('/results', methods=['post'])
def disp_results():
    print(request.form)
    data = {
        'name': request.form["name"],
        'location': request.form["dojo_location"],
        'language': request.form["favorite_language"],
        'comments' : request.form["comments"]
    }
    return render_template('results.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
