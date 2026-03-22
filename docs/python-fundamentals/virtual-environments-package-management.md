# Virtual Environments & Package Management

A virtual environment isolates Python and its packages per project so dependencies do not conflict. Use one env per project.

## Create a virtual environment

- Recommended built-in tool: `venv` (ships with Python 3)

```bash
# Windows (PowerShell)
py -3 -m venv .venv

# macOS/Linux
python3 -m venv .venv
```

Common env folder names: `.venv`, `venv`, `.env`. `.venv` is nice because many tools auto-detect it and it’s easy to gitignore.

## Activate / Deactivate

- Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
# later
deactivate
```

- Windows (cmd):

```bat
.venv\Scripts\activate.bat
deactivate
```

- macOS/Linux (bash/zsh/fish):

```bash
source .venv/bin/activate
deactivate
```

When active, your shell prompt usually shows `(.venv)` and `python`/`pip` point to the env.

## Verify interpreter and pip

```bash
python -V
python -c "import sys; print(sys.executable)"
pip -V
```

All should resolve inside `.venv`.

## Installing packages with pip

```bash
# install latest
pip install requests

# pin exact version
pip install "requests==2.32.3"

# upgrade in-place
pip install --upgrade requests

# uninstall
pip uninstall requests
```

List what’s installed:

```bash
pip list
```

## requirements.txt workflow

- Create a lock-like list from current env:

```bash
pip freeze > requirements.txt
```

- Recreate env elsewhere:

```bash
pip install -r requirements.txt
```

- Use constraints to cap versions without forcing install:

```bash
pip install -r requirements.in -c constraints.txt
```

Tip: Keep `requirements.in` (unpinned, human-edited) and compile to a pinned `requirements.txt` with tools like `pip-tools` (optional).

## pyproject.toml workflow (modern builds)

Modern packages declare metadata and build backends in `pyproject.toml` (PEP 517/518). For pure “app” projects you can still benefit:

- Editable install for local packages:

```bash
pip install -e .
```

This reads `pyproject.toml` (or legacy `setup.cfg`/`setup.py`) and installs your project into the env in “editable” mode.

## Dev vs prod dependencies

- Simple approach: separate files:
  - `requirements.txt` (runtime)
  - `requirements-dev.txt` (dev/test tools)

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

## Platform-specific notes (Windows)

- If `Activate.ps1` is blocked, enable script execution for your user:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Alternative environment managers (optional)

- `conda`/`mamba`: env + package manager (great for data science, non-Python libs).
- `pipenv`, `poetry`: combine env + dependency management + locking. Prefer one workflow per repo to avoid confusion.

## Best practices

- One `.venv` per project; commit `requirements*.txt` or `poetry.lock`/`Pipfile.lock`, but never commit the `.venv` itself.
- Pin exact versions for reproducibility in apps; use ranges for libraries.
- Keep your `pip`, `setuptools`, and `wheel` updated in new envs:

```bash
pip install --upgrade pip setuptools wheel
```

[<- Back to Python fundamentals](./python-fundamentals.md)
