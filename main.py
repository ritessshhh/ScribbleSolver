from flask import Flask, render_template, url_for, request, redirect, jsonify
import base64
from model.model import solution, Solver
from PIL import Image
import io
import numpy as np

app = Flask(__name__)

roots = ''
equ = ''
alert_message = ''

@app.route('/')
def index():
    return render_template("index.html", alert=alert_message)

@app.route('/save_image', methods=['POST'])
def save_image():
    global roots, equ
    data = request.get_json()
    image_b64_str = data['image']
    image_b64_str = image_b64_str.split(",")[1]
    image_bytes = base64.b64decode(image_b64_str)
    image = Image.open(io.BytesIO(image_bytes))
    img_np = np.array(image)
    equ, roots = solution(img_np)

    return jsonify({'redirect': '/show_alert'})


@app.route('/solve_equation', methods=['POST'])
def solve_equation():
    global roots, equ
    equ = str(request.form.get('equation'))
    solution1 = Solver(equ)
    roots = solution1.solveEquation()
    return redirect('/show_alert')

@app.route('/show_alert')
def show_alert():
    global roots, equ, alert_message
    if roots == 'Equation not readable. Tip: Have more space between each numbers.':
        alert_message = '<div class="alert alert-danger" role="alert"><svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" fill="currentColor" class="bi bi-x-octagon-fill" viewBox="0 0 16 16">   <path d="M11.46.146A.5.5 0 0 0 11.107 0H4.893a.5.5 0 0 0-.353.146L.146 4.54A.5.5 0 0 0 0 4.893v6.214a.5.5 0 0 0 .146.353l4.394 4.394a.5.5 0 0 0 .353.146h6.214a.5.5 0 0 0 .353-.146l4.394-4.394a.5.5 0 0 0 .146-.353V4.893a.5.5 0 0 0-.146-.353L11.46.146zm-6.106 4.5L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 1 1 .708-.708z"/> </svg> Your equation: ' + equ + " " + roots +'</div>'
    else:
        alert_message = '<div class="alert alert-success" role="alert">Equation Solved! 🎉 Values of x for '+ equ +' are:<br>' + roots.__str__() + '</div>'

    return render_template("index.html", alert=alert_message)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
