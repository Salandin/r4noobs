VERSION=`python setup.py --version`

default:
	@echo "Specify one of: serve, publish_docs, publish_package, clean-pyc, clean-build"

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

serve:
	/usr/bin/env mkdocs serve -s -a 0.0.0.0:8000

publish_docs:
	/usr/bin/env mkdocs gh-deploy

publish_package:
	@echo Build python distribution
	python setup.py sdist bdist_wheel
	@echo "Publish to PyPI at https://pypi.python.org/pypi/mkdocs-windmill-dark"
	@echo "Version in setup.py is $(VERSION)"
	@echo "Git tag is `git describe --tags`"
	@echo "Run this manually: /usr/bin/env twine upload dist/mkdocs-windmill-dark-$(VERSION).tar.gz dist/mkdocs_windmill_dark-$(VERSION)-py3-none-any.whl"


.PHONY: clean-pyc clean-build serve publish_docs publish_package
