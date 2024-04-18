install:
        poetry install

publish:
        poetry publish --dry-run

package-install:
        python3 -m pip install --user dist/*.whl
