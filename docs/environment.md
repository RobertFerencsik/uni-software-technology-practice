# Setup the environment for collaborating

This is only a recommendation and help. 
Feel free to add and modify.

## Visual Studio Code

First download & install [vscode][vscode]. 

Now in the next step you should install the extensions for your work.

Or profiles, they are pretty useful.

- [Python extension][python-e] this adds language support, debugging, and virtual environments
- [Markdown Preview extension][markdown-p-e] using the `CTRL + SHIFT + v` makes a preview from your makrdown.
- [Markdown profile][markdown-p] for better support



## python

Download and install [python install manager][p-install-m]

Make a python virtual environment in the root of the project, so you don't install packages globally. Usefull so there is no library version conflicts between your projects. Also you can then freeze your environment making it reproducible after you installed your packages.

- `python -m venv .venv`                create the environment
- `.venv\Scripts\activate`               activate on windows
- `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` give permission to run scripts (in powershell)
- `deactivate`
- `pip freeze > requirements.txt`       save the libraries and their versions into the req file
- `pip install -r requirements.txt`     download and install the libs with the version specified in the req file

## git 

Download and install [git][git].

Settings for git, use with parameter to set, without parameter to print:

``` bash
man git-config
git config --global --list
git config --global user.name "Your Full Name"
git config --global user.email "yourmail@example.com"
```
``` bash
git config --global core.editor "code --wait"
git config --global diff.tool vscode
git config --global difftool.vscode.cmd "code --wait --diff \"$LOCAL\" \"$REMOTE\""
git config --global difftool.prompt false
git config --global help.autocorrect 1
git config --global rebase.autoStash true
```

you can set aliases for git commands. If you write the alias the defined code runs.

`git config --global alias.lg "log --oneline --graph --decorate --all"`


[vscode]: https://code.visualstudio.com/download
[python-e]: https://marketplace.visualstudio.com/items?itemName=ms-python.python
[markdown-p-e]: https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced
[markdown-p]: https://code.visualstudio.com/docs/configure/profiles#_doc-writer-profile-template
[p-install-m]: https://www.python.org/downloads/
[git]: https://git-scm.com/install/windows
[n++]: https://notepad-plus-plus.org/downloads/
