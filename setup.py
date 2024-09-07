from setuptools import setup

REQUIRES = [
    'curlify',
    'requests',
    'structlog',
    'allure-pytest'
]

setup(
    name='restclient',
    version='0.0.1',
    packages=['restclient'],
    url='https://github.com/DoraSigulia/restclient.git',
    license='MIT',
    author='Daria Sigulya',
    author_email='',
    install_requires=REQUIRES,
    description='restclient with allure and logger'
)
