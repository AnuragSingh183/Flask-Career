from flask import Flask, render_template, jsonify

app = Flask(__name__)

Jobs = [{
    'id': 1,
    'title': "Data Analyst",
    'location': "Bengaluru, India",
    'salary': "Rs. 10,00,000"
}, {
    'id': 2,
    'title': "Android Developer",
    'location': "Bengaluru, India",
    'salary': "Rs. 15,00,000"
}, {
    'id': 3,
    'title': "Data Scientist",
    'location': "Gurgaon, India",
    'salary': "Rs. 10,00,000"
}, {
    'id': 4,
    'title': "Software Developer",
    'location': "New York City, USA",
    'salary': "$200,000"
}]


@app.route("/")
def hello():
  return render_template("home.html", jobs=Jobs, company_name="Jedi")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(Jobs)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
