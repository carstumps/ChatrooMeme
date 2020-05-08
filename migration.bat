#set FLASK_APP=SMSite.py
#flask db init
#flask db migrate -m "users table"
#flask db migrate -m "posts table"
flask db upgrade
