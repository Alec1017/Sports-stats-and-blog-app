# Sports stats and blog app

## Getting Started

1) clone project

2) cd into application

```bash
cd sports-stats-and-blog-app
```

3) install from Pipfile

```bash
pipenv install
```

4) activate Pipenv shell

```bash
pipenv shell
```

5) run the application

```bash
python run.py
```

app will be running on http://localhost:5000 by default


## Database usage

This app uses MongoDB with Flask-Pymongo.
If necessary, documents can be added to mongo collections via the flask shell.

```bash
export FLASK_APP=run.py
flask shell
from app import mongo
mongo.db.users.find({'username': 'test'})
```
