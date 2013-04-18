# YeaNay.io
A project that allows people to explore polarization in Congress and its effects on legislative productivity.

# Installation
- Clone the repo
- Set up a virtualenv for the project
- install dependencies via `pip install -r requirements.txt`
- copy local settings and fill in database/secret-key settings (`cp local_settings.example.py local_settings.py`)
- sync the database (`python manage.py syncdb`)
- load ideology data (`python manage.py load_ideology`)

Should be all set after that - not much there yet in terms of views or pages.