![Ruff](https://github.com/hgb-bin-proteomics/pyXLMS-template/workflows/Ruff%20Linting%20and%20Formatting/badge.svg)
![Ty](https://github.com/hgb-bin-proteomics/pyXLMS-template/workflows/Type-checking%20with%20ty/badge.svg)
![Pytest](https://github.com/hgb-bin-proteomics/pyXLMS-template/workflows/Testing%20with%20pytest/badge.svg)

# Template Repository for pyXLMS projects

A template repository for python scripts and projects using [pyXLMS](https://github.com/hgb-bin-proteomics/pyXLMS).

## Checklist

- [ ] Use [uv](https://docs.astral.sh/uv/) for python project and dependency management.
- [ ] Write your code in `main.py` or any other python file.
- [ ] \[Optionally\] setup tests in `tests/`.
- [ ] Replace data in `data` with your own data \[or delete if you don't have data\].
- [ ] Adjust the `LICENSE` and/or choose a different license.
- [ ] Adjust this `README.md` to your needs!

**We don't automatically bump pyXLMS versions anymore, please either run:**

- `uv lock --upgrade`
- or `uv lock --upgrade-package pyxlms`

**...after cloning the template to make sure you are running the latest pyXLMS version!**

## Getting Help

- Help for pyXLMS: [github.com/hgb-bin-proteomics/pyXLMS](https://github.com/hgb-bin-proteomics/pyXLMS)
- Help for this template:
  - [uv](https://docs.astral.sh/uv/): Python project and dependency management.
  - [ruff](https://astral.sh/ruff): Python linter and formatter.
  - [ty](https://docs.astral.sh/ty/): Python type checker.
  - [pytest](https://docs.pytest.org/en/stable/): Python testing suit.
  - [GitHub Actions](https://docs.github.com/en/actions): Used for running the above automatically.
  - You may also want to check out [this](https://github.com/michabirklbauer/python_template) template which was used as a basis.
- Contact: [micha.birklbauer@fh-hagenberg.at](mailto:micha.birklbauer@fh-hagenberg.at)
