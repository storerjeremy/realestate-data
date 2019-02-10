import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='realestate-data',
    version='0.1.0',
    author='Jeremy Storer',
    author_email='storerjeremy@gmail.com',
    description='Realestate Data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/storerjeremy/realestate-data',
    packages=setuptools.find_packages(),
    install_requires=[
        'schematics',
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
