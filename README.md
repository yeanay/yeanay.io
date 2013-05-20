# YeaNay.io
A project that allows people to explore polarization in Congress and its effects on legislative productivity.

# Installation
- Clone the repo
- Run `vagrant up` to initialize the virtual-machine (will download/install dependencies)
- SSH into VM with `vagrant ssh`
- Add postgres user for project - some combination of the following commands usually works
  - set password for postgres: `sudo passwd postgres`
  - change to postgres user: `su postgres`
  - create user with password (remember these since this is what goes in the local_settings.py file): `createuser -P -s -e <USERNAME>` and enter password at prompt
- copy local settings and fill in database/secret-key settings/NYT_KEY (`cp local_settings.example.py local_settings.py`)
- sync the database (`python manage.py syncdb`)
- load ideology data via fixtures (`python manage.py loaddata ideology`)

- start the server `python manage.py runserver [::]:8000

- navigate to polarization data from browser `http://localhost:8001/polarization/`