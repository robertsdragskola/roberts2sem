from flask from flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Sveiki!"

 if __name__=='_main_':
  app.run(port=5000)







print('Sveiki!')