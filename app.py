from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/') # Перша сторінка
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/car1') # Друга сторінка
def car1():
    return render_template("car1.html")


@app.route('/car2') # Третя сторінка
def car2():
    return render_template("car2.html")


@app.route('/car3') # Четверта сторінка
def car3():
    return render_template("car3.html")


@app.route('/car4') # П'ята сторінка
def car4():
    return render_template("car4.html")


@app.route('/car5') # П'ята сторінка
def car5():
    return render_template("car5.html")


@app.route('/user/<string:name>/<int:id>') # сторінка з user
def user(name, id):
    return "user:" + name + " - " + str(id)


if __name__ == "__main__":
    app.run(debug=True) # показує помилк на сторінці які є в коді.