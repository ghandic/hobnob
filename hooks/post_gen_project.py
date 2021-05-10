message = """
Great, you're all set up, just run the following commands:

cd {{ cookiecutter.project_name }}
docker-compose up --build -d
docker exec -it {{ cookiecutter.project_name }} bash -c "poetry run poe init"
docker exec -it {{ cookiecutter.project_name }} bash

git add .
git commit -m "Initial commit"
git branch -M main
{%- if cookiecutter.git_service == "gitlab" -%}

git remote add origin https://gitlab.com/{{cookiecutter.repo_author}}/{{ cookiecutter.project_name }}.git
{%- elif cookiecutter.git_service == "github" -%}

git remote add origin https://github.com/{{cookiecutter.repo_author}}/{{ cookiecutter.project_name }}.git
{% endif %}
git push -u origin main
"""
print(message)
