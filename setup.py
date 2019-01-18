from setuptools import find_packages, setup

setup(
    name='flower_bed_designer',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'cerberus',
        'python-dotenv'
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
        ],
    },
)
