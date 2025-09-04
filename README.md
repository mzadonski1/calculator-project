# CLI Calculator (Python)

A clean, well-structured command-line calculator for a programming class. Includes a simple CLI, separated math operations, and basic tests.

## How to run (Windows + PowerShell)

```powershell
# 1) Create and activate a virtual env (optional but recommended)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2) (Optional) Install test tools
pip install -r requirements.txt

# 3) Run the calculator
python -m calculator.cli
```

## Project structure

```
calculator-project/
├─ .gitignore
├─ requirements.txt
├─ README.md
├─ src/
│  └─ calculator/
│     ├─ __init__.py
│     ├─ operations.py
│     └─ cli.py
└─ tests/
   └─ test_operations.py
```

## Git quick-start (local → GitHub)

```bash
# Initialize a repo and make the first commit
git init
git branch -M main
git add .
git commit -m "Initial commit: CLI calculator"

# Create a new empty repo on GitHub (via the website), then connect:
git remote add origin https://github.com/YOUR-USER/calculator-project.git
git push -u origin main

# Create a feature branch for changes (good practice)
git switch -c feature/exponent
# ... make code changes ...
git add -A
git commit -m "Add exponent operation and menu option"
git push -u origin feature/exponent

# Open a Pull Request on GitHub and merge it, then:
git switch main
git pull
git tag -a v1.0.0 -m "First release"
git push origin v1.0.0
```

## Running tests

```bash
pytest -q
```
```
