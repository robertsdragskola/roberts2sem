from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teksts")
def teksts():
    return render_template("teksts.html")

@app.route("/saraksts")
def saraksts():
    saraksts = ["sigma", "el primo", "johny"]
    bildes = ["https://upload.wikimedia.org/wikipedia/en/thumb/0/09/Skibidi_toilet_screenshot.webp/237px-Skibidi_toilet_screenshot.webp.png", "https://static.wikia.nocookie.net/brawlstars/images/0/04/El_Primo_Skin-Default.png/revision/latest?cb=20200225131129", "https://www.webwise.ie/wp-content/uploads/2018/04/Fortnite.jpg"]
    kopejais_saraksts = [["sigma","https://upload.wikimedia.org/wikipedia/en/thumb/0/09/Skibidi_toilet_screenshot.webp/237px-Skibidi_toilet_screenshot.webp.png"], ["el primo","https://static.wikia.nocookie.net/brawlstars/images/0/04/El_Primo_Skin-Default.png/revision/latest?cb=20200225131129"], ["johny", "https://www.webwise.ie/wp-content/uploads/2018/04/Fortnite.jpg"]]
    return render_template("saraksts.html", vardi=saraksts, bildes = bildes, garums = len(kopejais_saraksts), visi=kopejais_saraksts)


@app.route("/bilde")
def bilde():
    return render_template("bilde.html")


@app.route("/info")
def info():
    return render_template("īnfo.html")



if __name__ == '__main__':
    app.run(port = 5000)





