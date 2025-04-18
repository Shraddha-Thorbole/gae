from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pincode = request.form.get("zipCode")
        if not pincode or not pincode.isnumeric() or len(pincode) != 6:
            return render_template("index.html", error="Incorrect Pin Code (String / False Code entered)")

        url = f"https://api.postalpincode.in/pincode/{pincode}"
        response = requests.get(url)
        data = response.json()

        if data[0]["Status"] == "Success":
            post_office = data[0]['PostOffice'][0]['State']
            name = data[0]['PostOffice'][0]['Name']
            block = data[0]['PostOffice'][0]['Block']
            district = data[0]['PostOffice'][0]['District']
            return render_template("results.html", post_office=post_office, name=name, block=block, district=district)
        else:
            return render_template("error.html")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)