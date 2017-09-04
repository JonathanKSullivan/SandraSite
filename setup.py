from setuptools import setup

setup(
    name='qualitaxas',
    packages=['qualitaxas'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-restful',
        'flask_assets'
    ],
)
