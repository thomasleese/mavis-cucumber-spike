# Mavis testing spike

## Installing

```shell
$ mise install
$ pip install -U pip uv
$ uv run playwright install
```

## Configuring

Create a `behave.ini` file with the following parameters:

```ini
[behave.userdata]
base_url = ...

basic_auth_username = ...
basic_auth_password = ...

admin_username = ...
admin_password = ...

nurse_username = ...
nurse_password = ...

superuser_username = ...
superuser_password = ...
```

## Linting

```shell
$ uv run ruff format
```

## Running

```shell
$ uv run behave -D browser=firefox
$ uv run behave -D browser=chromium
$ uv run behave -D browser=webkit -D "device=iPhone 6"
```
