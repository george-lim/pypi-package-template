# Python Template

[![releases](https://img.shields.io/github/v/release/george-lim/python-template)](https://github.com/george-lim/python-template/releases)
[![ci](https://github.com/george-lim/python-template/workflows/CI/badge.svg)](https://github.com/george-lim/python-template/actions)
[![codecov](https://codecov.io/gh/george-lim/python-template/branch/main/graph/badge.svg)](https://codecov.io/gh/george-lim/python-template)
[![license](https://img.shields.io/github/license/george-lim/python-template)](https://github.com/george-lim/python-template/blob/main/LICENSE)

## [Usage](#usage) | [Features](#features) | [Examples](#examples) | [CI/CD](#cicd)

Python Template is a template repository that provides CI/CD workflows for Python applications.

## Usage

Choose `george-lim/python-template` as the template when creating a new repository.

## Features

Python Template provides a `README.md`, `LICENSE`, `.gitignore`, and two workflows for GitHub Actions.

## Examples

There are no examples to provide for Python Template.

## CI/CD

### Pipeline

There are two workflows in this repository. Each workflow supports manual triggering.

The `CI` workflow is automatically triggered whenever there is push activity in `main` or pull request activity towards `main`. It has two jobs:

1. Lint the codebase with GitHub's [Super-Linter](https://github.com/github/super-linter).
2. Run unit tests with `pytest`, generate a code coverage report, and upload the report to [Codecov](https://codecov.io/gh/george-lim/python-template).

The `CD` workflow is automatically triggered whenever there is a tag pushed to the repository. It has one job:

1. Create a GitHub release with the tag.

### Codecov

You will need to authorize Codecov with your GitHub account in order to upload code coverage reports.

Follow the [Codecov GitHub Action](https://github.com/codecov/codecov-action) to see how to configure the action for private repositories.
