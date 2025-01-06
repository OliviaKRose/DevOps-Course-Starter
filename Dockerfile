#turn previous single stage Dockerfile into a multi-stage Dockerfile
#perform common operations, dependency install etc
FROM python:3.12 as base
RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /opt/app
COPY pyproject.toml poetry.toml /opt/app/
ENV PATH=$PATH:/root/.local/bin/
RUN poetry install
COPY . /opt/app



#configure for prod
FROM base as production
ENV FLASK_DEBUG=false
ENTRYPOINT poetry run flask run --host 0.0.0.0

#configure for dev
FROM base as development
ENV FLASK_DEBUG=true
ENTRYPOINT poetry run flask run --host 0.0.0.0

# add bind mount for hot reloading  
# docker run --publish 8000:5000 -it --env-file .env .en--mount "type=bind,source=$(pwd)/todo_app,target=/opt/app/todo_app" todo-app:dev
