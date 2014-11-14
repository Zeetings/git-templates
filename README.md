# Git templates

This project provides the git template to use internally at Zeetings.

Git hooks:
* pre-push: It makes sure that shared branches like *master* and *dev* are never force pushed.
* commit-msg: It adds automatically the branch name to each commit message. This is useful when we need to go through history because it helps us to identify and group commits.

It also provides aliases and default options for push and pull operations

### Installation

1. Clone the repo
2. Make sure you can run the installer: `chmod u+x install.py`
3. Run `install.py`.
4. Create a repository, it will use our template.
5. For old repositories run this command: `git init`.

### Behind the scenes

When you run the installer the following things happen:

1. The contents of `template` folder are copied to `~/.git-templates`.
2. Your global git configuration is updated to use `~/.git-templates` as the default template.
3. Your global git configuration is updated with some default options for push and pull operations.
4. Global aliases are added to your git installation.
