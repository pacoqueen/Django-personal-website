# Django-personal-website

This is a fork from Django-based personal website created by [Vlad Moroshan](https://github.com/vladislavalerievich/Django-personal-website).

[Live site](https://qinn.es).

## Installation and Running

* Run the command `git clone <repository-url>` to have this repository locally in your computer.
* `sudo apt-get install -y mariadb-server libmariadb-dev`
* `sudo apt install libjpeg-dev zlib1g-dev`
* Change into the new directory.
* `source bin/activate`
* `python3 -m pip install --upgrade defusedxml olefile`
* `python3 -m pip install --upgrade pip`
* `python3 -m pip install --upgrade Pillow`
* `pip install -r requirements.txt`
* Create or copy (from dev computer) secrets file: `scp my_secrets/secrets.py user@remote_host:Django-personal-website/my_secrets; scp my_secrets/definitions.py user@remote_host:Django-personal-website/my_secrets`
* [Optional] (from dev computer): `scp db.sqlite3 user@remote_host:Django-personal-website/`
* Run the command `python manage.py runserver`.
* Open your web browser and enter the adress of your local server (usually http://127.0.0.1:8000).
