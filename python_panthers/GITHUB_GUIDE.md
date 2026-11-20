# Python Panthers setup and GitHub guide

## 1. Open and run the project

1. Extract `python_panthers.zip`.
2. In VS Code, open the extracted `python_panthers` folder. You should see `wanisha_python_panthers.py` and the `data` folder in the Explorer.
3. Open **Terminal → New Terminal**. Check that Python 3 and Git are available.

```sh
python --version
git --version
```

If a command is missing, install the corresponding program and reopen VS Code. If `python` is unavailable but Python 3 is installed, try `py -3` on Windows or `python3` on macOS or Linux. Use that same command wherever the guide shows `python`. [Python downloads](https://www.python.org/downloads/) · [Git downloads](https://git-scm.com/downloads) · [VS Code downloads](https://code.visualstudio.com/download)

Run the assignment and the selection checks.

```sh
python wanisha_python_panthers.py
python scratch.py
```

The assignment should report 11 players, 99.5 credits, Saim Ayub as captain, and Faheem Ashraf as vice-captain. The validator should end with `All team selection rules met.`

## 2. Create the GitHub repository

Sign in to the account that will own the project. Create a repository named `python-panthers` and choose the visibility required for submission. Leave GitHub’s README, `.gitignore`, and license options unchecked when creating it. The project already includes its own README and `.gitignore`. [Create a repository](https://github.com/new) · [GitHub upload instructions](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)

## 3. Commit and push

In the VS Code terminal, run these commands from the extracted project folder. If this folder already has its own Git repository, skip `git init` and check the branch with `git branch --show-current`. Use that branch name in the push commands.

```sh
git init -b main
git add .
git status
git commit -m "Add Python Panthers fantasy cricket project"
```

If Git reports `Author identity unknown`, set the name and email for commits in this repository, then retry the commit. Replace the example values with your name and your GitHub email or GitHub-provided no-reply address.

```sh
git config user.name "Your Name"
git config user.email "your-email@example.com"
git commit -m "Add Python Panthers fantasy cricket project"
```

Copy the HTTPS URL from the GitHub repository page. Replace `YOUR-USERNAME` below with the GitHub account name that owns the repository. If the repository name is different, use the exact URL from the page.

```sh
git remote add origin https://github.com/YOUR-USERNAME/python-panthers.git
git remote -v
git push -u origin main
```

If Git opens a browser sign-in, use an account with write access to the repository. Git Credential Manager supports HTTPS sign-in. [GitHub credential setup](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git)

## 4. Fix common Git errors

### `remote origin already exists`

Run `git remote -v`. If `origin` already points to the correct repository, run `git push -u origin main`. If it points to the wrong repository, change the URL before retrying. [GitHub remote instructions](https://docs.github.com/en/get-started/git-basics/managing-remote-repositories)

```sh
git remote set-url origin https://github.com/YOUR-USERNAME/python-panthers.git
git push -u origin main
```

### `The current branch has no upstream branch`

Push the current branch and set its tracking branch. After the first successful push, `git push` is enough for later commits.

```sh
git push -u origin HEAD
```

### `fetch first` or `non-fast-forward`

GitHub has commits your local branch needs to include. Verify `origin` with `git remote -v`, then fetch and merge the remote `main` branch. Substitute the actual branch name if the repository uses a different default. [GitHub non-fast-forward instructions](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors)

```sh
git fetch origin
git merge --no-edit origin/main
```

If Git says `refusing to merge unrelated histories`, the local folder and the GitHub repository were initialized separately. After confirming that `origin` points to your Python Panthers repository, run the merge with the option that permits joining those histories. [Git merge options](https://git-scm.com/docs/merge-options)

```sh
git merge --allow-unrelated-histories --no-edit origin/main
```

If the merge stops with conflicts, run `git status` and open the listed files in VS Code. Edit each conflicted file to keep the content you want, save it, then stage the resolved files and finish the merge.

```sh
git add .
git commit --no-edit
```

After the merge succeeds, run `python wanisha_python_panthers.py` and `python scratch.py` again, then push.

```sh
git push -u origin main
```

### `Repository not found` or `Permission denied`

Check the repository URL with `git remote -v`. Open that repository on GitHub and confirm you are signed in with the account that owns it or has write access.

## 5. Verify and share the repository

Refresh the GitHub repository page. Check that `wanisha_python_panthers.py`, `README.md`, and the `data` folder appear on the default branch. Share the repository page URL when submitting the project. If the repository is private, give the reviewer access before sharing the URL.

For future edits, run the Python checks again, review the changes with `git status`, and commit and push.

```sh
git add .
git commit -m "Describe your change"
git push
```
