from setuptools import setup

setup(
    name='node',
    packages=['node'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_cors',
    ],
)
