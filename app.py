
from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        try:
            S = float(request.form.get("S", 2500))
            m = float(request.form.get("m", 3))
            U1 = float(request.form.get("U1", 11000))
            U2 = float(request.form.get("U2", 13800))
            uk = float(request.form.get("uk", 6.5))
            pk = float(request.form.get("pk", 25000))

            Sf = S * 1000 / m
            I1 = S * 1000 / (3**0.5 * U1)
            I2 = S * 1000 / (3**0.5 * U2)
            Uf2 = U2 / (3**0.5)
            ua = pk / (10 * S)
            ur = (uk**2 - ua**2)**0.5

            result = {
                "Sf": round(Sf, 3),
                "I1": round(I1, 3),
                "I2": round(I2, 3),
                "Uf2": round(Uf2, 3),
                "ua": round(ua, 3),
                "ur": round(ur, 3)
            }
        except:
            result = {"error": "Помилка обчислення. Перевірте введені значення."}
    return render_template("section_1_1.html", result=result)

@app.route("/details")
def details():
    return render_template("calc_details.html")

@app.route("/section/<name>")
def section(name):
    try:
        return render_template(f"{name}.html")
    except:
        return "Шаблон не знайдено", 404

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    # ensure the graphs are in the static folder
    for fname in ["graph_mass_vs_beta.png", "graph_loss_vs_beta.png", "graph_dims_vs_beta.png"]:
        src = f"/mnt/data/{fname}"
        dst = os.path.join("static", fname)
        if os.path.exists(src):
            with open(src, "rb") as fsrc, open(dst, "wb") as fdst:
                fdst.write(fsrc.read())
    app.run(debug=True)
