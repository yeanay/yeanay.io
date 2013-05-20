#!/usr/bin/env bash

apt-get update

apt-get install -y python-dev
apt-get install -y python-setuptools
apt-get install -y python-pip

apt-get install -y postgresql
apt-get install -y postgresql-server-dev-9.1

apt-get install -y git

apt-get install -y libxml2
apt-get install -y libxslt1.1

pip install -r /usr/local/yeanay/requirements.txt
