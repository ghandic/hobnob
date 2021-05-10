# Cookiecutter project

## Initial project setup

```bash
cookiecutter <URL>
cd <project_name>
docker-compose up --build -d
docker exec -it <project_name> bash
poe init
```

## Precommit hooks

- Linting (auto fixes most things)
- Safety checking
- Type annotation checking
- Gitmoji - adds useful emojis to commit messages 😊

## Utility scripts

- `poe clean` - Cleans the project of old cache files
- `poe test` - Runs the full unit test suite with coverage
- `poe lint` - Runs the linting on the full project and auto fixes most things
- `poe docs` - Serves mkdocs on http://0.0.0.0:8000
- `poe init` - Used when first initializing a repo, sets up precommit hooks etc.
