from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("https://giffy-lake-three.vercel.app/api/image.py", code=302)
