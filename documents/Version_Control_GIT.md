# Version Control with Git

This document outlines the version control strategy used for the Call Type Predictor project. It includes details on initializing the repository, managing branches, merging, and handling changes, as well as best practices we adopted to ensure a smooth workflow in Git.

## Repository Initialization

To start the project, we first initialized a Git repository. This allows us to track all changes, collaborate efficiently, and revert to previous versions if needed.

```bash
git init
```

After initializing the Git repository, the next step was to add a remote repository where all team members could push their changes.

```bash
git remote add origin https://github.com/yourusername/yourrepository.git
```

## Branching Strategy

We used a feature-branch workflow to manage development. This strategy involves creating a new branch for each feature or bug fix, which ensures that the main branch always contains stable and deployable code.

### Creating a Feature Branch

Whenever starting work on a new feature, we created a new branch from `main`:

```bash
git checkout -b feature_branch_name
```

This command creates a new branch and switches to it. Work on the feature is isolated in this branch, which allows for focused development without affecting the main line.

## Committing Changes

Frequent commits were made to ensure that changes were adequately documented and could be reviewed. Each commit message was written to reflect the changes clearly:

```bash
git add .
git commit -m "A concise commit message describing the change"
```

## Merging and Pull Requests

Once a feature was completed, it was merged back into the main branch through a pull request (PR), which allows for code review. Here’s how we prepared the feature branch for merging:

### Updating the Feature Branch

Before merging, we made sure the feature branch was updated with the latest main branch changes to minimize conflicts:

```bash
git checkout main
git pull
git checkout feature_branch_name
git merge main
```

### Creating a Pull Request

A pull request was created on GitHub, where team members could review the changes. After approval, the PR was merged into the main branch.

```bash
git checkout main
git merge feature_branch_name
git push origin main
```

## Reverting Changes

If we needed to undo changes, we used `git revert` for reversing specific commits, or `git reset` to rollback to a specific state:

### Reverting a Commit

```bash
git revert commit_hash
```

This command creates a new commit that undoes the changes made in `commit_hash`.

### Resetting to a Previous Commit

For undoing multiple changes or completely reverting the repository to a previous state:

```bash
git reset --hard commit_hash
git push -f origin main
```

## Best Practices

1. **Commit Often**: Small, frequent commits make it easier to identify issues and roll back changes without significant disruption.
2. **Clear Commit Messages**: Each commit message should be informative and reflect the made changes.
3. **Code Reviews**: All merges should be done through PRs reviewed by at least one other team member.

## Conclusion

By adhering to these Git practices, we maintained a robust and flexible development environment. This strategy supported our team's collaborative efforts and helped manage the project's complexity efficiently.

---