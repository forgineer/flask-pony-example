from setuptools import setup

setup(
    name='pony-blog',
    version='1.0.0',
    author='forgineer',
    description='The basic blog app built in the Flask tutorial with Pony ORM integration.',
    url='https://github.com/forgineer/flask-pony-example',
    license='MIT License',
    packages=['pony_blog'],
    python_requires='>=3.8',
    install_requires=[
        'Flask',
        'pony',
    ],
)
