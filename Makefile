help:
	@echo Makefile Commands:
	@echo \'make remove_and_publish\' to remove last distribution and publish the actual distribution

remove_last_dist:
	rm -rf build/ dist/ pulib.egg-info/

package_dist:
	python3 setup.py sdist bdist_wheel

publish:
	twine upload dist/*

remove_and_publish: remove_last_dist package_dist publish
