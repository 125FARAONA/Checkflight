from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulación de usuario
USER = {"username": "user", "password": "pass123"}

# Simulación de vuelo
flights = [
    {"id": 1, "type": "Ordinario", "from": "Santo Domingo", "to": "New York", "seat": "Economy", "price": "Gratis"},
    {"id": 2, "type": "Ida y vuelta", "from": "Santo Domingo", "to": "Miami", "seat": "Business", "price": "Gratis"},
]

# Checklist inicial
tasks = [
    {"task": "Check-in online", "done": False},
    {"task": "Documentos listos", "done": False},
    {"task": "Maleta preparada", "done": False},
    {"task": "Llega al aeropuerto", "done": False},
    {"task": "Abordaje completado", "done": False},
]

@app.route("/", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == USER["username"] and password == USER["password"]:
            return redirect(url_for("dashboard"))
        else:
            error = "Usuario o contraseña incorrectos"
    return render_template("login.html", error=error)

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        flight_id = int(request.form["flight"])
        selected_flight = next((f for f in flights if f["id"] == flight_id), None)
        return render_template("checklist.html", flight=selected_flight, tasks=tasks)
    return render_template("dashboard.html", flights=flights)

@app.route("/update_task/<int:task_id>")
def update_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = True
    # Revisar si todas las tareas están completadas
    if all(t["done"] for t in tasks):
        return redirect(url_for("completed"))
    return redirect(url_for("dashboard"))

@app.route("/completed")
def completed():
    # Reset tasks
    for t in tasks:
        t["done"] = False
    return render_template("completed.html")

if __name__ == "__main__":
    app.run(debug=True)
