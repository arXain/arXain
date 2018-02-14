from setuptools import setup

setup(
    name='pyXain',
    packages=['pyXain'],
    include_package_data=True,
    install_requires=[
        'requests',
        'ipfsapi'
    ],
)
