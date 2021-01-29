from flask import Flask, render_template
from get_containt import GetData

get_info = GetData()

app = Flask(__name__)

@app.route('/')
def home():
    data = get_info.all_data
    return render_template("index.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)
