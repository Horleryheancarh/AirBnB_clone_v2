#!/usr/bin/env bash
# Configure Nginx and copy files to it
apt update -y
apt install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hello From Nginx" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}' /etc/nginx/sites-available/default
service nginx start
exit 0
