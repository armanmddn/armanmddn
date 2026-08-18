SHELL := /bin/sh
COMPOSE := docker compose

.PHONY: bootstrap up down reset logs ps migrate test lint check

bootstrap:
	@test -f .env || cp .env.example .env
	$(COMPOSE) up --build --wait

up: bootstrap

down:
	$(COMPOSE) down --remove-orphans

reset:
	$(COMPOSE) down --volumes --remove-orphans

logs:
	$(COMPOSE) logs --follow

ps:
	$(COMPOSE) ps

migrate:
	$(COMPOSE) run --rm migrate

test:
	python -m pytest
	npm --prefix apps/finance-miniapp test

lint:
	python -m ruff check .
	python -m mypy services packages apps/finance-bot
	npm --prefix apps/finance-miniapp run lint

check: lint test
