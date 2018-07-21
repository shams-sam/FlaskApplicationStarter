# FlaskApplicationStarter
Flask Application Using Docker Running on Uwsgi for NLP Engine

- application runs on docker
- uses uwsgi along with flask

### Build
```bash
cp .env.sample .env
docker-compose build
```

### Run
```bash
docker-compose up -d
```

### Stop
```bash
docker-compose down
```

### Debug
```bash
# run in verbose mode
docker-compose up

# list the containers running
docker-compose ps

# probing inside the container
docker exec -it <container-name> bash
```
