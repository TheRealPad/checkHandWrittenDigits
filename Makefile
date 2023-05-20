.PHONY: start server server_build

FILE_SERVER=server/app.py
PYTHON_DEPENDENCIES_FILE=requirements.txt

start: server_build server

server_build:
	@pip install -r $(PYTHON_DEPENDENCIES_FILE)

server:
	@python $(FILE_SERVER)