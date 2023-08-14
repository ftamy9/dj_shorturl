# To run localy you need to create and activate venv and install the requirements.txt.
# To run on docker flow this guid:
sudo docker-compose up -d --build
sudo docker-compose exec db psql --username=surl_u --dbname=surl_d
# the password is surl_p
sudo docker-compose exec web python manage.py migrate --noinput
# (if there is a problem about DB run sudo docker-compose down -v) then 
# start from the 1st command
# there are 4 web services that you can test the APIs acourding to the following samples (but you need to replace SERVER-OR-LOCAL-IP):

------------------

curl -X POST -d '{ "id": "farhan_10", "password_hash": "123" }' -H "Content-Type: application/json" http://SERVER-OR-LOCAL-IP:80/user/signup

curl -i -X PUT -d '{ "id": "farhan_10", "password_hash": "123" }' -H "Content-Type: application/json" http://SERVER-OR-LOCAL-IP:80/user/signup

# Replace the token (eyJ1c....) in the next. 
curl -i -X POST -d '{ "url": "http://icanhazip.com" }' -H "Authorization: Basic eyJ1c2VyX2lkIjogImZhcmhhbl8xMCIsICJ0aW1lc3RhbXAiOiAiMjAyMy0wOC0xM1QwNzoyMzoyMS4xNDMzNDEiLCAic2lnbiI6ICI5YzFkZWJjZWY4ZjQ5OTUxZDg5ZjJkMjQ5YWQ5YzFjYjI1MDU1ODc2YjNhMzExYTJhN2Q2NDk5ODQxYjBjNWRlZjJkN2MyYWRlZjViYmY5MGZjOTk1ZDA5MGM4MTZlYjIyNDc0MTQzNzUyZDY2ZTk2NjliZmVlMDUzNzU0NGNjYyJ9" -H "Content-Type: application/json" http://SERVER-OR-LOCAL-IP:80/user/signup

# Replace the token (eyJ1c....) and the uuid (e9652e37....) in the next. 
curl -iL -X GET -H "Authorization: Basic eyJ1c2VyX2lkIjogImZhcmhhbl8xMCIsICJ0aW1lc3RhbXAiOiAiMjAyMy0wOC0xM1QwNzoyMzoyMS4xNDMzNDEiLCAic2lnbiI6ICI5YzFkZWJjZWY4ZjQ5OTUxZDg5ZjJkMjQ5YWQ5YzFjYjI1MDU1ODc2YjNhMzExYTJhN2Q2NDk5ODQxYjBjNWRlZjJkN2MyYWRlZjViYmY5MGZjOTk1ZDA5MGM4MTZlYjIyNDc0MTQzNzUyZDY2ZTk2NjliZmVlMDUzNzU0NGNjYyJ9" -H "Content-Type: application/json" http://SERVER-OR-LOCAL-IP:80/user/signup/e9652e37-c747-495c-b465-fd09d38e66df

------------------
