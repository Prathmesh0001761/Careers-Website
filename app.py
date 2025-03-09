from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    "title":"Data Analyst",
    'location':'Mumbai, india',
    'salary':'RS 15,00,000'
  },
  {
    'id':2,
    "title":"Data Scientist",
    'location':'Navi Mumbai, india',
    'salary':'RS 18,00,000'
  },
  {
    'id':3,
    "title":"SDE",
    'location':'Kalyan, india',
    'salary':'RS 25,00,000'
  },
  {
    'id':4,
    "title":"FrontEnd engineer",
    'location':'san francisco, USA',
    'salary':'RS 65,00,000'
  },
]

@app.route("/")
def hello():
  return render_template('home.html',jobs=JOBS,company_name = "Jovian")

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)