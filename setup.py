from setuptools import setup

setup(
    name='car_service_tracker',
    version='1.0',
    py_modules=['car_service_tracker'],
    entry_points={
        'console_scripts': [
            'car-service-tracker = lab1:main',
        ],
    },
)
