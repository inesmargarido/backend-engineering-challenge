from setuptools import find_packages, setup

setup(
    name='unbabel_cli',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'unbabel_cli=avg_delivery_time:main'
        ]
    }
)