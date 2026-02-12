from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/accordion")
def accordion():
	return render_template("sample/accordion.html")

@app.route("/carousel")
def carousel():
	return render_template("sample/carousel.html")

@app.route("/modal")
def modal():
	return render_template("sample/modal.html")

@app.route("/collapse")
def collapse():
	return render_template("sample/collapse.html")

@app.route("/dial")
def dial():
	return render_template("sample/dial.html")

@app.route("/dismiss")
def dismiss():
	return render_template("sample/dismiss.html")

@app.route("/drawer")
def drawer():
	return render_template("sample/drawer.html")

@app.route("/dropdown")
def dropdown():
	return render_template("sample/dropdown.html")

@app.route("/popover")
def popover():
	return render_template("sample/popover.html")

@app.route("/tabs")
def tabs():
	return render_template("sample/tabs.html")

@app.route("/tooltip")
def tooltip():
	return render_template("sample/tooltip.html")

@app.route("/input-counter")
def input_counter():
	return render_template("sample/input-counter.html")

@app.route("/datepicker")
def datepicker():
	return render_template("sample/datepicker.html")

if __name__ == '__main__':
	app.run(debug=True)