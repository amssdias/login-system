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

1. Download Pipenv through the terminal window ***(make sure you have [Python][python-download] installed)***:

	```python
     pip install pipenv  # For Windows
     brew install pipenv # For MacOs
     sudo apt install pipenv # For Debian Buster+
     sudo dnf install pipenv # For Fedora

    ```
    
2. After installing pipenv, download the files and in the terminal window, go to the project directory which contain the **Pipfile** and **Pipfile.lock** and run:

	```python
    pipenv install
    ```
    This will create a virtual environment with all the modules needed.

3. We must have this virtual environment activated to run our program, through the terminal window:

	```python
    pipenv shell # To run the virtual environment
    exit         # To close the virtual environment
    ```

If any doubts here's a link to some more explanations: [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html)



## :mag_right: Usage

On your terminal window, go to the project directory with the Pip files and type: 

```python
pipenv shell
python manage.py runserver
```

Paste this link on your browser:
**http://127.0.0.1:8000/auth/login**
