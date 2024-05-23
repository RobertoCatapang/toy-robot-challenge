# toy-robot-challenge


## Introduction

A web app that allows the user to move a robot within a grid. It contains two parts, a **Python** backend as the API and a **Svelte** Frontend as the UI.

## Requirements
Before you start running or developing the program make sure you have the following below installed.

For API:
```
python 3.11+
poetry
```

For UI:
```
node
npm
```

## Installation

Additional libraries are required. Create a virtual environment and use poetry for installing the packages.

### Creating a virtual environment:
```bash
create a virtual env
python3.11 -m venv venv
. venv/bin/activate
```

### Installing packages:

For API:
```bash
poetry install
```

For UI:
```
cd ui
npm install
```

## Usage
Both the API and UI need to be running to use the web app.

For API:
```bash
. venv/bin/activate
uvicorn api.app:app --reload
```

For UI, In another terminal run:
```bash
cd ui
npm run dev
```

## Testing
Note: Testing is only availble for API.

Testing to produce coverage report:
```bash
pytest -vv --cov=toy-robot --cov=tests --cov-report=term-missing --cov-report=xml  tests/
```

or doing a quick test
```bash
pytest tests/
```
