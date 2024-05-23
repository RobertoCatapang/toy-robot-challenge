# toy-robot-challenge


requirements

for api
python 3.11
poetry

for ui
node
npm
svelte

create a virtual env
python3.11 -m venv venv
. venv/bin/activate


poetry install

uvicorn api.app:app --reload

test:
	pytest -vv --cov=toy-robot --cov=tests --cov-report=term-missing --cov-report=xml  tests/
	or
	pytest tests/

linting

mypy --install-types --non-interactive api/
mypy api
black api --line-length 88
flake8 api
bandit -r api/


npm create svelte@latest ui
cd ui
npm install
npm run dev

Next steps:
  1: cd ui
  2: npm install
  3: git init && git add -A && git commit -m "Initial commit" (optional)
  4: npm run dev -- --open