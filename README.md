# flask-pony-example
The basic blog app built in the Flask tutorial with Pony ORM integration.

## Pony Blog
The basic blog app built in the Flask [tutorial](https://flask.palletsprojects.com/tutorial/).

### Install
Clone the repository.

```
$ git clone https://github.com/pallets/flask-pony-example
```

Open the repository and create a virtual environment (Windows example).

```
$ cd flask-pony-example
$ py -3 -m venv .venv
$ .venv\Scripts\activate.bat (or Activate.ps1)
```

Install Pony ORM.

```
$ pip install .
```

### Run
```
$ flask --app pony_orm init-db
$ flask --app pony_orm run --debug
```

Open http://127.0.0.1:5000 in a browser.
