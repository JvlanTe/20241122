from flask import Flask, render_template, request, redirect, url_for
from database import get_tasks, add_tasks, show_tasks, edit_task, delete_task

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        tasks = get_tasks()
        return render_template("index.html", tasks=tasks)
    else:
        title = request.form["title"]
        content = request.form["content"]
        due_date = request.form["due_date"]
        status = request.form["status"]
        add_tasks(title, content, due_date, status)
        return redirect(url_for("index"))

@app.route("/show/<int:id>")
def show(id):
    task = show_tasks(id)
    return render_template("show.html", task=task)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "GET":
        task = show_tasks(id)
        return render_template("edit.html", task=task)
    else:
        title = request.form["title"]
        content = request.form["content"]
        due_date = request.form["due_date"]
        status = request.form["status"]
        edit_task(id, title, content, due_date, status)
        return redirect(url_for("index"))


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    delete_task(id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)