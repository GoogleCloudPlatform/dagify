from setuptools import setup, find_packages

def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

def read_file(file):
   with open(file) as f:
        return f.read()

long_description = read_file("README.md")
requirements = read_requirements("requirements.txt")

setup(
    name='airship',
    version='0.0.1',    
    description='A python package to assist in converting enterprise scheduler\
         formats to Apache Airflow DAGs',
    long_description_content_type = "text/markdown",  # If this causes a warning, upgrade your setuptools package
    long_description = long_description,
    url='https://github.com/KonradSchieban/cntrlm-to-airflow/issues/new',
    author='Konrad Schieban, Tim Hiatt, Google Cloud PSO',
    author_email='airship-code@google.com',
    license='Apache License',
    license_files='LICENCE',
    packages = find_packages(exclude=["test"]),  # Don't include test directory in binary distribution
    install_requires = requirements,

    classifiers=[
        'Development Status :: 1 - Planning',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Code Generators',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',  
        'Programming Language :: Python :: 3.11',
    ],
)