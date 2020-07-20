upload:
	twine check dist/*
	twine upload dist/*
	rm -rf dist/*
