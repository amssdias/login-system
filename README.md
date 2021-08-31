[python-download]: https://www.python.org/downloads/
[django-link]: https://www.djangoproject.com/

![Python Badge](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Python Badge](https://img.shields.io/badge/Django-3.2.4-092E20?logo=django)


# Login System Template

<!-- <p align="center">
    <img src="media/website.png" width="900px">
</p> -->

A basic template of a login system so you can use the template in any web app with just minimal changes to quickly build the web apps. Nowadays every website requires their customers to create accounts therefore this template will be very useful.

### Built with

![Django Badge](https://img.shields.io/badge/-Django-092E20?style=for-the-badge&labelColor=black&logo=django&logoColor=white)


## :hammer: Getting started

### Pre requisites

- [Python][python-download] - 3.9 or up
- [Django][django-link] - 3.2.4


### Installation

#### Clone the project

```
git clone https://github.com/amssdias/login-system
cd login-system
```

#### Configure settings(email)

Must fill the ".env_sample_file" file, so users can receive activation links and to reset passwords.


#### Install dependencies & activate virtualenv

1. Pipenv ***(make sure you have [Python][python-download] installed)***:

	```python
     pip install pipenv  # For Windows
     brew install pipenv # For MacOs
     sudo apt install pipenv # For Debian Buster+
     sudo dnf install pipenv # For Fedora

    ```
    
2. Install packages:

	```python
    pipenv install # will create a virtual environment with all the modules needed
    ```

3. Activate virtualenv and apply migrations:

	```python
    pipenv shell # To activate the virtual environment

    python manage.py makemigrations
    python manage.py migrate
    ```

If any doubts here's a link to some more explanations: [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html)



## :mag_right: Usage


```python
pipenv shell
python manage.py runserver
```

Paste this link on your browser:
**http://127.0.0.1:8000/auth/login**


## Features

- Log in
	- Via username and password
- Create an account
- Profile activation email
- Reset password
- Resend and activation link
- Change password