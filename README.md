# simple_streaming
App that stores messages in Redis and provides access to those messages via an HTTP REST API.


Steps to test simple_streaming:

# clone repo
1) git clone git@github.com:angmar33/simple_streaming.git

# move to main directory and install the requirements
2) cd file_path/simple_streaming && pip install -r requirements.txt

# install and run redis
3) https://redis.io/docs/getting-started/

4) redis-server 

# run the server using uWSGI
5) uwsgi --http :5000 --master --workers 10 --wsgi-file config/app.py

# Now HTTP client can connect and retrieve the events as they're sent
6) http --stream GET http://127.0.0.1:5000/message/chatroom

# send a message using POST endpoint
7) http --json --stream POST http://127.0.0.1:5000/message/chatroom source=jd content="perfect stream tested" 
