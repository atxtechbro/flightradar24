```markdown
# Contributing to Flightradar24 Data Analyzer

First off, thank you for considering contributing to Flightradar24 Data Analyzer. It's people like you that make Flightradar24 Data Analyzer such a great tool.

## Where do I go from here?

If you've noticed a bug or have a feature request, make one! It's generally best if you get confirmation of your bug or approval for your feature request this way before starting to code.

## Fork & create a branch

If this is something you think you can fix, then fork and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```sh
git checkout -b 325-add-japanese-localisation
```

## Get the test suite running

Make sure you have the necessary dependencies:

```sh
pip install -r requirements.txt
```

Run the tests:

```sh
python -m unittest
```

## Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first.

## Make a Pull Request

At this point, you should switch back to your master branch and make sure it's up to date with Flightradar24 Data Analyzer's master branch:

```sh
git remote add upstream https://github.com/atxtechbro/flightradar24.git
git checkout master
git pull upstream master
```

Then update your feature branch from your local copy of master, and push it!

```sh
git checkout 325-add-japanese-localisation
git rebase master
git push --set-upstream origin 325-add-japanese-localisation
```

Finally, go to GitHub and [make a Pull Request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) :D

## Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

To learn more about rebasing in Git, there are a lot of [good](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) [resources](https://www.atlassian.com/git/tutorials/merging-vs-rebasing) but here's the suggested workflow:

```sh
git checkout 325-add-japanese-localisation
git pull --rebase upstream master
git push --force-with-lease 325-add-japanese-localisation
```

## Merging a PR (maintainers only)

A PR can only be merged into master by a maintainer if:

1. It is passing CI.
2. It has been approved by at least one maintainer. If it was a maintainer who opened the PR, only an additional maintainer can approve it.
```
