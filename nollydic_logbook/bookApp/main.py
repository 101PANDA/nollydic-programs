from flask import Flask
from flask import render_template, request
from models.person import Person
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        form = request.form

        name = form.get("fullName")
        date = datetime.now().isoformat()
        role = form.get("position")
        department = form.get("department")
        phone = form.get("telNo")

        person = Person()
        person.update(name=name, datetime=date, role=role, department=department, phone=phone)

        return f"{name} {date} - {role} {department} -- {phone}"
    return render_template("mainform.html")

if __name__ == "__main__":
    app.run("0.0.0.0", "5000")