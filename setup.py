from setuptools import setup, find_packages

setup(
    name='mishnabot',
    version="1.1.0",
    description='Discord bot that posts a random sugye per day.',
    long_description='Discord bot that posts a random sugye per day.',
    long_description_content_type='text/markdown',
    url='https://github.com/subalterngames/mishnabot',
    author_email='subalterngames@gmail.com',
    author='Esther Alter',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    packages=find_packages(),
    include_package_data=True,
    keywords='mishnah talmud jewish discord bot',
    install_requires=['discord.py==1.7.3'],
)
