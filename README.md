# Dagster MVP
This repo is intended to function as an MVP for a Dagster instance. The idea is to have this repo demonstrate boilerplate functionality of Dagster to enable any user to quickly spin up their workflow orchestration setup.


## Running with Docker
To run the environment on your machine the repo is setup to use Docker. Simply clone the repo to your machine and execute the command below 

```
docker-compose up -d --build
```

This will spin up containers that you will need to start working with this repository. If successful, it should look something like this on your Docker Desktop dashboard

![Screenshot 2023-05-01 at 22 51 20](https://user-images.githubusercontent.com/10533379/235496568-f949770b-b786-4065-aa31-6f0b482d26be.png)

The deployment makes use of 4 different containers running
- Dagit UI
- Dagster Daemon
- Dagster gRPC
- PostgreSQL backend

Please navigate to on your favorite browser to see the Dagit UI. The above `docker compose` command also mounted the local GitHub repo to the Docker container, you are now free to make code changes and contribute to ther repo. :) 