# https://flask.palletsprojects.com/en/2.0.x/tutorial/install/

# https://flask.palletsprojects.com/en/2.0.x/tutorial/install/#id1
from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)


