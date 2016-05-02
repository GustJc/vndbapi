from pip.req import parse_requirements
from setuptools import setup, find_packages

install_reqs = parse_requirements('requirements.txt', session=False)
# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

EXCLUDE_FROM_PACKAGES = []

setup(
    name='vndbapi',
    version='0.0.1',
    url='https://github.com/gustjc/vndbapi',
    author='Gustavo Jaruga Cruz',
    author_email='darksshades@hotmail.com',
    description='VNDB API Wrapper',
    license='LICENSE.txt',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    zip_safe=False,
    long_description=open('README.md').read(),
    install_requires=reqs,
    test_suite="tests.run.runtests",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
