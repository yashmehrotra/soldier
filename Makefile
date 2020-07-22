pybuild:
	rm -rf dist/*
	python setup.py sdist bdist_wheel

upload:
	twine check dist/*
	twine upload dist/*
	rm -rf dist/*
