# URL Shortener

The URL Shortener is a simple full-stack containerised application that converts a provided URL into a shorter URL. Any data that is saved (ie remembering of shortened URLs and how to redirect the user to the original URL) persists across service restarts. The entire stack comprises of React, Django and PostgreSQL. 

## Usage

1. To use this application, clone the repository into a directory. 

2. Set up the environmental variables by creating a `.env` file in the root, `/frontend` and `/backend` directories respectively. For example, for the main and backend files, it should look something like this:

```
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_PASS=postgres
```

For `/frontend/.env`, it should look like this:

```
REACT_APP_BACKEND=http://localhost:8000
REACT_APP_HOST=http://localhost:3000
```

3. After setting the environmental variables, you can run `docker-compose build` to build the images. Then, run `docker-compose up` to start the containers. 
NOTE: if the backend is starting before the database is ready, increase the sleep time in `/backend/wait-for-postgres.sh`. This can be handled with a more specific script in the future.

4. In a separate terminal, run `docker ps` to list the running containers

```
CONTAINER ID   IMAGE                   COMMAND                  CREATED          STATUS          PORTS                                       NAMES
32b143f4e986   omni_project_frontend   "docker-entrypoint.s…"   13 seconds ago   Up 11 seconds   0.0.0.0:3000->3000/tcp, :::3000->3000/tcp   omni_project_frontend_1
59257f9f6a4e   omni_project_backend    "/wait-for-postgres.…"   14 seconds ago   Up 12 seconds   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   omni_project_backend_1
533af3acf595   postgres                "docker-entrypoint.s…"   15 seconds ago   Up 14 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   omni_project_db_1
```

5. Run `docker exec -t -i <container-id> bash` to access the container.

6. Run `python3 ./backend/manage.py migrate` to migrate the models into the database.

7. Your web application should now be running properly at `http://localhost:8000`.

![Webpage image](/assets/webpage.png)

