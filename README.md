<p align="center">
  <img src="https://user-images.githubusercontent.com/82912148/221045488-3bc889c1-ef7a-4ea6-a0a6-20ac0a538173.png" width="500">
</p>

<!-- Back to Top Navigation Anchor -->
<a name="readme-top"></a>

<!-- Project Shields -->
<div align="center">

  [![Contributors][contributors-shield]][contributors-url]
  [![Forks][forks-shield]][forks-url]
  [![Stargazers][stars-shield]][stars-url]
  [![Issues][issues-shield]][issues-url]
  [![MIT License][license-shield]][license-url]
  [![Twitter][twitter-shield]][twitter-url]
</div>


<div align="center">
  <h1>Flask REST API for Pizza Delivery Service and its deployment to Heroku</h1>
</div>

<div>
  <p align="center">
    <a href="https://github.com/BrodaOJ56/flask-delivery-pizza-api#readme"><strong>Explore the Docs »</strong></a>
    <br />
    ·
    <a href="https://github.com/BrodaOJ56/flask-delivery-pizza-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/BrodaOJ56/flask-delivery-pizza-api/issues">Request Feature</a>
  </p>
</div>

---

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#About-Flask-REST-API-for-Pizza-Delivery-Service">About Flask REST API for Pizza Delivery Service</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#Deployed-With">Deployed With</a></li>
      </ul>
    </li>
    <li><a href="#What-I-learnt">What I learnt</a></li>
    <li><a href="#How-to-run-the-project-on-Local">How to run the project on Local</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#Connect-With-Me">Connect With Me</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
  <p align="right"><a href="#readme-top">back to top</a></p>
</details>

---

<!-- About the Blog -->
## About Flask REST API for Pizza Delivery Service

This is a GitHub repository for a Pizza Flask API that provides functionality for ordering pizzas from a hypothetical pizza delivery service.

The API provides several endpoints for various actions related to pizza ordering. Some of these endpoints include; sign up, login, place order, get all orders, delete order etc.

This Flask API could be a good starting point for someone looking to build a simple pizza ordering system or learn more about building APIs with Flask.


<p align="right"><a href="#readme-top">back to top</a></p>

### Built With:

![Python][python]
![Flask][flask]
![SQLite][sqlite]

### Deployed With:

![Heroku][heroku]

<p align="right"><a href="#readme-top">back to top</a></p>

---
<!-- Lessons from the Project -->
## What I learnt 
- How to set up a Flask API with Flask-RESTX
- Databases with Flask-SQLAlchemy
- JWT Authentication with Flask-JWT-Extended
- Environment variables with Python-Decouple
- Database migrations with Flask-Migrate
- How to write Unit Tests with Unittest and PyTest
- Documenting REST APIs with SwaggerUI and Flask-RESTX
- Error Handling with Werkzeug
- Flask API Deployment via Heroku

<p align="right"><a href="#readme-top">back to top</a></p>

---
<!-- GETTING STARTED -->
## How to run the project on Local

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
---


<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- License -->
## License

Distributed under the MIT License. See <a href="https://github.com/BrodaOJ56/flask-delivery-pizza-api/blob/main/LICENSE">LICENSE</a> for more information.

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Contact -->
## Connect With Me

OLUBUNMI OLUWATOBI JAMES - [@ItzOfficialOJ](https://twitter.com/ItzOfficialOJ)


<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Acknowledgements -->
## Acknowledgements

This project was made possible by:

* [AltSchool Africa School of Engineering](https://altschoolafrica.com/schools/engineering)
* [Caleb Emelike's Flask Lessons](https://github.com/CalebEmelike)
* [GitHub Student Pack](https://education.github.com/globalcampus/student)

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Markdown Links & Images -->
[contributors-shield]: https://img.shields.io/github/contributors/BrodaOJ56/flask-delivery-pizza-api.svg?style=for-the-badge
[contributors-url]: https://github.com/BrodaOJ56/flask-delivery-pizza-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BrodaOJ56/flask-delivery-pizza-api.svg?style=for-the-badge
[forks-url]: https://github.com/BrodaOJ56/flask-delivery-pizza-api/network/members
[stars-shield]: https://img.shields.io/github/stars/BrodaOJ56/flask-delivery-pizza-api.svg?style=for-the-badge
[stars-url]: https://github.com/BrodaOJ56/flask-delivery-pizza-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/BrodaOJ56/flask-delivery-pizza-api.svg?style=for-the-badge
[issues-url]: https://github.com/BrodaOJ56/flask-delivery-pizza-apiissues
[license-shield]: https://img.shields.io/github/license/BrodaOJ56/flask-delivery-pizza-api.svg?style=for-the-badge
[license-url]: https://github.com/BrodaOJ56/flask-delivery-pizza-api/blob/main/LICENSE.txt
[twitter-shield]: https://img.shields.io/badge/-@ItzOfficialOJ-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/ItzOfficialOJ
[twitter-url]: https://twitter.com/ItzOfficialOJ
[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[sqlite]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
[Heroku]: https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white

