docker run -it --rm -d -p 8080:80 --name web webserver

docker build -t webserver .
docker run -it --rm -d -p 8080:80 --name web webserver

docker-compose build
docker-compose up -d

nslookup ns.main.com
dig @127.0.0.1 ns.main.com

ps -ef | grep nginx
ps -C nginx -f
docker top web

/usr/share/nginx/html

nginx -s reload