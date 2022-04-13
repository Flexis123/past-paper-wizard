from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blueprints import blueprints

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

for bprint in blueprints:
    app.register_blueprint(bprint)

if __name__ == '__main__':
    db.create_all()
    app.run()

