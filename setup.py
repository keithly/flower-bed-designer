from setuptools import find_packages, setup

setup(
    name='flower_bed_designer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'voluptuous',
        'python-dotenv'
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
        ],
    },
)
