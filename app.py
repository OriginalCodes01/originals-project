from flask import Flask, render_template

app = Flask(__name__)
TALENTS = [
  {
    "id": 1,
    "title": "Film making" 
    },
 {
    "id": 1,
    "title": "Oration" 
  },
{
  "id": 2,
  "title": "Video editing" 
},
{
  "id": 3,
  "title": "Programming" 
},
{
  "id": 4,
  "title": "Fashion" 
},
{
  "id": 5,
  "title": "Sweet man" 
}
         ]

@app.route("/")
def hello_world():
  return render_template("home.html",
                         Talents=TALENTS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
