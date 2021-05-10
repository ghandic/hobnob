<h1 align="center">
   <strong>{{cookiecutter.project_name}}</strong>
</h1>

<p align="center">
    <a href="https://codecov.io/gh/{{cookiecutter.repo_author}}/{{cookiecutter.project_name}}" target="_blank">
        <img src="https://img.shields.io/codecov/c/github/{{cookiecutter.repo_author}}/{{cookiecutter.project_name}}?color=%2334D058" alt="Coverage">
    </a>
    <a href="https://{{cookiecutter.repo_author}}.github.io/{{cookiecutter.project_name}}" target="_blank">
        <img src="https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat" alt="Docs">
    </a>
    <a href="https://pypi.org/project/{{cookiecutter.project_name}}/" target="_blank">
        <img src="https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg" alt="PyPI Latest Release">
    </a>
    <br />
    {%- if cookiecutter.git_service == "gitlab" -%}
    <a href="https://gitlab.com/{{cookiecutter.repo_author}}/{{cookiecutter.project_name}}/-/blob/main/LICENSE" target="_blank">
        <img src="https://img.shields.io/gitlab/license/{{cookiecutter.repo_author}}/{{cookiecutter.project_name}}.svg" alt="License">
    </a>
    {%- elif cookiecutter.git_service == "github" -%}
    <a href="https://github.com/{{cookiecutter.repo_author}}/{{cookiecutter.project_name}}/blob/main/LICENSE" target="_blank">
        <img src="https://img.shields.io/github/license/{{cookiecutter.repo_author}}/{{cookiecutter.project_name}}.svg" alt="License">
    </a>
    {% endif %}
    <a href="https://github.com/psf/black" target="_blank">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">
    </a>
</p>

{{cookiecutter.description}}

## Main Features

- ... # TODO: Add features

## Installation

<div class="termy">

```console
$ pip install {{cookiecutter.project_name}}

---> 100%
```

</div>

## Usage

### Basic 😊

```python
import {{cookiecutter.project_name}}

...
```

Results in ... # TODO: Add example

```python
# TODO: Add example
```

## Credits

- # TODO: Add credits

## License

* [MIT License](/LICENSE)
