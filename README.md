# About
This is a docker container that uses Flask and MongoDB to host a TO-DO list.

# Installation
```
# Clone the gitub repo
git clone https://github.com/ondrejhonus/flask-db-docker.git

# Go into the 
cd flask-db-docker

# Create a virtual enviroment
python -m venv .venv

# Activate the virtual enviroment
. .venv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Run an build the app
docker-compose up --build
```

### Then you can run the container with
```
docker-compose up
```