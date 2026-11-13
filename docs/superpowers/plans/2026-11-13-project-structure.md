# Project structure checklist

**Goal:** a small Python project skeleton suitable for GitHub, without an API or strategy implementation at this stage.

**Structure:** an installable package in `src/trade_bot/`, tests in `tests/`, and documentation in English. No application dependencies before the first API feature.

**Design:** [Scope and structure](../../architecture.md).

- [x] Create package metadata and initialize the Python package.
- [x] Add the README, test directory instructions, and architecture rationale.
- [x] Exclude secrets, virtual environments, and local data from Git.
- [x] Validate TOML, Python package imports, and Git ignore rules.

Verified at the project skeleton stage with Python 3.12.10: TOML parsing and package imports from `src` work, and seven local example paths are ignored by Git. `.env.example` and source code are not ignored. Editable installation had not yet been verified at that stage. Git checks required a command-scoped `safe.directory` setting because the sandbox user owned the `.git` directory.

Publishing to GitHub, commits, API integration, and business logic are outside the scope of this stage. Functional tests are not added for the directory structure alone.
