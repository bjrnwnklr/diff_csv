# Python Template

Python template set-up, covering my main set-up and workflow.

# How to use

-   Use as Template in GitHub when setting up a new repository
-   Customize the files to the new project

# Structure

```
.
├── .flake8
├── .github
│   └── workflows
│       └── main.yml
├── .gitignore
├── .vscode
│   └── settings.json
├── cli_app.py
├── README.md
├── package_name
│   ├── __init__.py
│   ├── core.py
│   └── utils.py
├── req_initial.txt
├── setup.py
└── tests
    ├── conftest.py
    ├── context.py
    └── test_core.py
```

# Files to customize before using

1. Change the package name and associated imports

-   Change the folder `package_name` to the desired package name
-   `setup.py`: Replace `package_name` and fill in the description, add dependencies to `install_requires`.
-   Change imports:
    -   `package_name` directory:
        -   `core.py`
        -   `utils.py`
    -   `tests` directory:
        -   `context.py`
        -   `conftest.py`
        -   `test_core.py`
    -   `cli_app.py`: (Template for a CLI app, using the functions from the `core` and `utils` modules.)

1. Add required packages to the `req_initial.txt` file

# Other python templates

-   [rochacbruno's python project template](https://github.com/rochacbruno/python-project-template)
-   [PyScaffold](https://github.com/pyscaffold/pyscaffold)
-   [gvisoc's python project template](https://github.com/gvisoc/python-project-template)
