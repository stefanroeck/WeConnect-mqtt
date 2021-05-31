import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()
INSTALL_REQUIRED = (HERE / "requirements.txt").read_text()
SETUP_REQUIRED = (HERE / "setup_requirements.txt").read_text()
TEST_REQUIRED = (HERE / "test_requirements.txt").read_text()

setup(
    name='weconnect-mqtt',
    packages=['weconnect_mqtt'],
    version=open("weconnect_mqtt/__version.py").readlines()[-1].split()[-1].strip("\"'"),
    description='CMQTT Client that publishes data from Volkswagen WeConnect',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Till Steinbach',
    keywords='weconnect, we connect, carnet, car net, volkswagen, vw, telemetry, mqtt, smarthome',
    url='https://github.com/tillsteinbach/WeConnect-mqtt',
    license='MIT',
    install_requires=INSTALL_REQUIRED,
    entry_points={
        'console_scripts': [
            'weconnect-mqtt = weconnect_mqtt.weconnect_mqtt:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
        'Topic :: System :: Monitoring',
        'Topic :: Home Automation',
    ],
    python_requires='>=3.7',
    setup_requires=SETUP_REQUIRED,
    tests_require=TEST_REQUIRED,
)
