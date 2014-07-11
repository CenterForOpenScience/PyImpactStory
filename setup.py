from setuptools import setup

setup(
    name='ImpactStory',
    version='0.1.0',
    author='Saman Ehsan and Erica Baranski',
    author_email='se8ea@virginia.edu and ericanbaranski@gmail.com',
    packages=['impact_story', 'impact_story.tests', 'impact_story.products'],
    url='http://pypi.python.org/pypi/ImpactStory/',
    license='LICENSE.txt',
    description='Python library for parsing impactstory profile information.',
    long_description=open('README.txt').read(),
    install_requires=[
        'requests == 2.3.0',
    ],
)

