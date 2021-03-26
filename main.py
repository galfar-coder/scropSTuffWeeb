from flask import *
import requests

app = Flask("")


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/show", methods=["GET","POST"])
def show():
	if request.method == "GET":
		return "oh, you didnt provide any URL in the <a href=\"/\"\>Home Page</a>", 451
	if request.method == "POST":
		print(request.form.get("url"))
		r = requests.get("https://plshelp.mkdev.ml/v1?url={0}".format(request.form.get("url")))
		if r.status_code != 400:
			re = r.json()

			return render_template("show.html", plugins=re["plugins"], errors=re["errors"], minecraft_version=re["minecraft_version"], server_software=re["server_software"], reload=re["reload"], needs_newer_java=re["needs_newer_java"])
		else:
			return "The URL enetred was wrong!", 400











app.run()