# Local runtime

## Prerequisites

- Docker Engine with Docker Compose v2
- GNU Make (optional; the equivalent Compose commands are shown below)
- Python 3.12 and Node.js 22 only when running `make check` on the host

A Telegram token is **not** required. The default `TELEGRAM_ADAPTER=fake` keeps polling local and deterministic. When testing live polling, put a development-only token in the untracked `.env` file and set `TELEGRAM_ADAPTER=live`.

## Start everything

From a clean checkout, run:

```bash
make up
```

This copies `.env.example` to the ignored `.env` file when necessary, builds the images, waits for PostgreSQL and Redis, applies migrations, then starts the API, fake bot, worker, and Mini App. The local endpoints are:

- API health: <http://localhost:8000/health/ready>
- Mini App: <http://localhost:5173>
- PostgreSQL: `localhost:5432` (local machine only)
- Redis: `localhost:6379` (local machine only)

The command without Make is:

```bash
cp -n .env.example .env

docker compose up --build --wait
```

## Common operations

```bash
make ps       # service state and health
make logs     # follow all logs
make migrate  # apply migrations again
make check    # lint and test using host toolchains
make down     # stop containers and preserve database data
make reset    # stop containers and delete local volumes
```

To inspect one service, use `docker compose logs api`, replacing `api` with `bot`, `worker`, `web`, `postgres`, or `redis`.

## Configuration and secrets

`.env.example` contains safe local defaults and the names of supported variables. `.env` and private-key formats are ignored by Git. Never put a real Telegram token, database credential, payment credential, or production secret in tracked files, test fixtures, screenshots, or logs.

`APP_SECRET_KEY` and the database password in the example are intentionally local-only values. Production must override every local credential through the deployment platform's secret manager.

## Dependency lock follow-up

The initial scaffold uses exact dependency versions but does not yet include an npm lockfile because the package registry is unavailable in the current build environment. Docker and CI therefore use `npm install`. Generate and commit `apps/finance-miniapp/package-lock.json` from an approved registry as soon as access is available, then switch both commands to `npm ci`.

## Expected startup evidence

A phase-F2 acceptance run should capture these commands:

```bash
make up
docker compose ps
curl --fail http://localhost:8000/health/ready
make check
docker compose run --rm migrate
```

All long-running application services must be running and healthy, both data stores must pass their health checks, migrations must exit successfully, and the test/lint suite must pass. Run `git status --ignored --short` to confirm `.env` remains ignored.
