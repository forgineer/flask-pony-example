# flask-pony-example
This repository features a comprehensive example of a Flask application seamlessly integrated with [Pony ORM](https://ponyorm.org/) for database interactions. This project evolves from the foundational blog app tutorial found on the official [Flask documentation page](https://flask.palletsprojects.com/), enhancing it by substituting the traditional SQL/SQLite approach with Pony ORM entities. Recognizing the gap in Pony ORM's documentation—particularly its lack of detailed examples on managing a complete Flask application with additional blueprints—this repository aims to bridge that gap. This example not only demonstrates the fundamental integration of Flask with Pony ORM but also delves into the nuances of scaling the application with more complex structures and functionalities, providing a practical, in-depth guide for developers looking to leverage Pony ORM's capabilities within their Flask projects.

## PonyBlog
"PonyBlog" is an enhanced version of the 'flaskr' blogging application, originally introduced in the Flask official documentation as a tutorial for new developers.

---

### Installation Instructions for Pony Blog

Follow these steps to get PonyBlog up and running on your local machine. This guide assumes you have Git and Python installed on your system.

#### 1. Clone the Repository

First, clone the Pony Blog repository from GitHub to your local machine using the following command:

```bash
git clone https://github.com/forgineer/flask-pony-example.git
```

#### 2. Navigate to the Project Directory

Change your current working directory to the `flask-pony-example` folder:

```bash
cd flask-pony-example
```

#### 3. Create and Activate a Python Virtual Environment

Create a virtual environment in the project directory. This isolates the project dependencies from your global Python environment.

To create a virtual environment, run:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows, use:

  ```bash
  .\venv\Scripts\activate
  ```

- On Unix or MacOS, use:

  ```bash
  source venv/bin/activate
  ```

#### 4. Install the Application and Dependencies

With the virtual environment activated, install Pony Blog and its dependencies using pip:

```bash
pip install .
```

This command installs everything needed to run the application, including Flask and Pony ORM.

#### 5. Run the Application

Start the Pony Blog application with Flask’s development server:

```bash
flask --app PonyBlog run
```

#### 6. Access the Application

Once the application is running, open your web browser and navigate to:

```
http://localhost:5000
```

You should now be able to interact with the Pony Blog application.
