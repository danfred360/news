 news

# run locally

Install python dependencies with poetry.

```bash
# download and install python dependencies to run the application
poetry install
# enter a terminal shell with access to python development environment
poetry shell
```

Use the `.env.example` file to create a `.env` file with your local secrets.

*.env*
```bash
APP_NAME=news
NEWS_API_KEY=apikeyhere
POSTGRES_USER=newsrw
POSTGRES_PASSWORD=nevergonnagiveyouup
POSTGRES_DB=news
DATABASE_URL=postgresql://myuser:mypassword@db/mydatabase
```

You can run the app in development mode by launching the `fastapi debugpy` launch configuration in vscode. This will do the following:

run postgres container with 

```bash
docker compose --profile development up
```

run python application at [http://127.0.0.1:57765](http://127.0.0.1:57765) with uvicorn. You can access the swagger page that lists the available endpoints [here](http://127.0.0.1:57765/docs).

# news api

> "Search worldwide news with code.
> Locate articles and breaking news headlines from news sources and blogs across the web with our JSON API"

- [terms of service](https://newsapi.org/terms)
- [getting started documentation](https://newsapi.org/docs/get-started)

