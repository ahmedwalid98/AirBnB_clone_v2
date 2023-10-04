#!/usr/bin/env bash
#scrip to setup web static

if [ ! -x /usr/sbin/nginx ]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
    sudo ufw allow 'Nginx HTTP'
    sudo echo 'Hello World!' > /var/www/html/index.html
    sudo service nginx start
fi
if [ ! -d "/data/" ]; then
    sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
fi

echo "Test file"| sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '16i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
