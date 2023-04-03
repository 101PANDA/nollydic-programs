from flask import Flask
from datetime import datetime
from flask import render_template, request, redirect, url_for
from models.person import Person
from models import storage

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        form = request.form

        name = form.get("fullName")
        date = datetime.now().isoformat()
        in_date = form.get("date")
        role = form.get("position")
        if role == "Staff":
            role_info = form.get("department")
        elif role == "Visitor":
            role_info = form.get("reason")
        phone = form.get("telNo")

        person = Person()
        person.update(name=name, datetime=date, role=role, role_info=role_info, phone=phone)
    return render_template("mainform.html")

@app.route("/admin", methods=["GET"])
def admin():
    logged_p = storage.today()
    visitor = []
    staff = []
    for person in logged_p:
        if person.role == "Staff":
            staff.append(person)
        elif person.role == "Visitor":
            visitor.append(person)
    return render_template("mbook_sheet.html", staffs=staff, visitors=visitor)

@app.route("/admin")
def auth():
    username = "ADMIN"
    password = "NOLLYDICadmin..."
    if username == request.form['username'] and password == request.form["password"]:
        return render_template("mbook_sheet.html")
    else:
        error = "Invalid username or password"
        return render_template("adminpage.html", error=error)

if __name__ == "__main__":
    app.run("0.0.0.0", "5000")