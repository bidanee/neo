run:
	python -m uvicorn main:app --host 0.0.0.0 --port 3000 --reload &
	pm2 start node_server/app.js

stop:
	pm2 stop all
	pkill -f "uvicorn"

rerun: stop run