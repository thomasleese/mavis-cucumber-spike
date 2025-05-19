# Mavis testing spike

## Installing

```shell
$ mise install
$ pip install -U pip uv
$ uv run playwright install
```

## Configuring

Create a `.env` file with the following parameters:

```ini
BASE_URL=...

BASIC_AUTH_USERNAME=...
BASIC_AUTH_PASSWORD=...

ADMIN_USERNAME=...
ADMIN_PASSWORD=...

NURSE_USERNAME=...
NURSE_PASSWORD=...

SUPERUSER_USERNAME=...
SUPERUSER_PASSWORD=...
```

## Linting

```shell
$ uv run ruff format
```

## Running

```shell
$ uv run --env-file .env behave -D "device=Desktop Firefox"
$ uv run --env-file .env behave -D "device=iPhone 6"
```

## Reporting

```shell
$ npm install
$ npx allure generate allure-results
$ npx allure open
```
