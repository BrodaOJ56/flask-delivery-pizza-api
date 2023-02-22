# Flask REST API for Pizza Delivery Service and its deployment to Heroku

This is a backend Flask REST API project for a Pizza delivery service and was deployed to heroku.


## How to run the project

Clone the project Repository
```
git clone https://github.com/BrodaOJ56/flask-delivery-pizza-api/
```

Enter the project folder and create a virtual environment
``` 
$ cd https://github.com/BrodaOJ56/flask-delivery-pizza-api/

$ python -m venv env 
```

Activate the virtual environment
``` 
$ source env/bin/actvate #On linux Or Unix

$ source env/Scripts/activate #On Windows 
 
```

Install all requirements

```
$ pip install -r requirements.txt
```

Run the project in development
```
$ export FLASK_APP=api/
$ export FLASK_DEBUG=1
$ flask run
```
Or 
``` 
python runserver.py
``` 
