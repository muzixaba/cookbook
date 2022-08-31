# Contributing
Contributors are urged to use the fork -> clone -> edit -> pul request workflow when making contributions.

## The Process
### 1 - Getting the Repo
- Create a personal fork of this project on GitHub
- Clone the fork from your account into your local machine.
- Verify that your copy of the remote repo is saved as `origin`. Run `git remote -v`
- Add the original repo as a remote called `upstream`. Run the following command `git remote add upstream upstream_url`.
- Pull changes from master or main branch into your local repo from upstream `git pull upstream master`

### 2 - Making Changes
- On your local repo, create a new branch that you'll use to make changes. Branch from `dev` or `develop` if it exists, else from `master` or `main`.
- Make your changes, remember to comment your code.
- Follow the style guide of the project. PEP8 is used for python code
- If tests exist, run them.
- Add and or adapt the tests if required.
- Optionally, you can squash your commits into a single commit

### 3 - Push up to GitHub
- Push your branch to you fork on GitHub, the remote `origin`.
- From your fork, open a Pull Request (PR). Target `develop` branch if exists, else `master` or `main`.

### 4 - Update your local repo
- Once your PR has been approved & merged, pull the changes from `upstream` to your local repo & delete your extra branches.

## Ideas for making your first contribution
- Add your name to the `contributors.md` file.