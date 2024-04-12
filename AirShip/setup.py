# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
    # If this causes a warning, upgrade your setuptools package
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/KonradSchieban/cntrlm-to-airflow/issues/new',
    author='Konrad Schieban, Tim Hiatt, Google Cloud PSO',
    author_email='airship-code@google.com',
    license='Apache License',
    license_files='LICENCE',
    # Don't include test directory in binary distribution
    packages=find_packages(exclude=["test"]),
    install_requires=requirements,

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
