
from flask import Flask, render_template, request, url_for, redirect, send_file
import tempfile
from natsort import natsorted
import pdfkit
import os


app = Flask(__name__)
config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')


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
    return render_template("section_4_1.html")


@app.route("/section/section_1_1", methods=["GET"])
def section_1_1_view():
    return redirect(url_for('index'))


@app.route("/section/<name>", methods=["GET", "POST"])
def section(name):
    try:
        template_file = f"{name}.html"
        print(f"[DEBUG] Rendering template: {template_file}")
        return render_template(template_file)
    except Exception as e:
        print(f"[ERROR] Failed to load template '{template_file}': {e}")
        return f"Шаблон не знайдено: {template_file}", 404


def get_existing_sections():
    templates_dir = 'templates'
    return sorted([
        f'section/{f.replace(".html", "")}'
        for f in os.listdir(templates_dir)
        if f.startswith('section_') and f.endswith('.html')
    ])


@app.route('/export_all', methods=['GET', 'POST'])
def export_all():
    if request.method == 'POST':
        sections = get_existing_sections()

        base_url = request.host_url.rstrip('/')
        urls = [f"{base_url}/{section}" for section in sorted(sections)]

        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as f:
            tmp_path = f.name

        options = {
            'javascript-delay': 3000,
            'enable-local-file-access': None,
            'window-status': 'katex-done',
            'no-stop-slow-scripts': '',
        }

        pdfkit.from_url(urls, tmp_path, options=options, configuration=config)

        return send_file(tmp_path, as_attachment=True, download_name="all_sections.pdf")

    return "Метод не дозволений", 405

@app.route('/export/<name>', methods=['POST'])
def export_section(name):
    try:
        # Проверяем, существует ли шаблон
        template_file = f"{name}.html"
        if not os.path.exists(os.path.join("templates", template_file)):
            return f"Шаблон {template_file} не знайдено", 404

        # Формируем правильный URL
        page_url = f"{request.host_url.rstrip('/')}/section/{name}"

        # Временный файл для PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as f:
            tmp_path = f.name

        options = {
            'javascript-delay': 3000,
            'enable-local-file-access': None,
            'window-status': 'katex-done',
            'no-stop-slow-scripts': '',
        }

        pdfkit.from_url(page_url, tmp_path, options=options, configuration=config)

        return send_file(tmp_path, as_attachment=True, download_name=f"{name}.pdf")

    except Exception as e:
        print(f"[ERROR] Failed to generate PDF for {name}: {e}")
        return "Помилка формування PDF", 500

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
