#============
# Basic App
#============
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'



# Running the app (Bash Commands)
export FLASK_APP=file_name.py
export FLASK_ENV=development
flask run


# Create model table(s) in bash
python3
from app_name import ModelName
obj = ModelName(arg1="value", arg2="value2")
db.session.add(obj)
db.session.commit()

# Query all models
ModelName.query.all()