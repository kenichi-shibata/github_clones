from setuptools import setup, find_packages

setup(
	name='GithubCloners',
	version='0.1',
	packages=[
		'cloners'
	],

	# Requires pygithub
	install_requires=[
		'PyGithub==1.35',
	],
	entry_points={
		'console_scripts': ['cloners=cloners.repos:main']
	},
	author='kenichi shibata',
	author_email='shibata.k@simplex.ne.jp',
	description='clone your github repos',
	license='MIT',
	python_requires='==3.4.3',
)