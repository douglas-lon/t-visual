from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pastel_e_bom'


from main import routes

