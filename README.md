# Destinations Catalog


It is a web application to manage general purpose categories and items belonging to these categories. It is focused on types of tourist attractions and destinations but could easily be used for other domains. 

It is written in Python(2.7.6) using the Python framework [Flask][flask-url] and various Flask extensions such as: [Flask-SQLAlchemy][flask-sqlalchemy-url], [Flask-WTF][flask-wtf-url], [Flask-Login][flask-login-url], [Flask-Principal][flask-principal-url] and [Flask-RESTful][flask-restfull-url].

The application provides:
 - Create, Read, Update and Delete (CRUD) operations for items and categories
 - the ability to upload and store images
 - local user authentication and authorization system
 - third-party OAuth2 authentication with Google and Facebook
 - JSON endpoints to access items and categories data (as an alternative way to access the information displayed in HTML)

To access the application online go to: [https://itemcatalog17.herokuapp.com/](https://itemcatalog17.herokuapp.com/)

## Instructions to run the application

To run the application locally you will need to:

 - Install the following dependencies using pip or your preferred package manager: 
```
     pip install Flask
     pip install flask-sqlalchemy
     pip install Flask-WTF
     pip install flask-principal
     pip install flask-login
     pip install flask-restful
     pip install google-api-python-client
```
 - Go to the application's source files and run ```python run-local.py``` from a console
 - Visit http://localhost:5000 in your browser.

**NOTES:**
 - The application has 2 local users by default, one regular user and one admin. These users and its credentials can be found in the populateDB.py file. 
 - To get an empty database or reset it to its original state (containing sample data), uncomment as needed, the following lines in \_\_init\_\_.py

```python 
    #with app.app_context():
        #db.drop_all()
        #db.create_all()
        #import populateDB as p
        #p.populateDB(db)
```    


[flask-url]: http://flask.pocoo.org/
[flask-sqlalchemy-url]: http://flask-sqlalchemy.pocoo.org/2.1/
[flask-wtf-url]: https://flask-wtf.readthedocs.io/en/stable/
[flask-login-url]: https://flask-login.readthedocs.io/en/latest/
[flask-principal-url]: http://pythonhosted.org/Flask-Principal/
[flask-restfull-url]: https://flask-restful.readthedocs.io/en/0.3.5/


