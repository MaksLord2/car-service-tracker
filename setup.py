from setuptools import setup

setup(
    name='car_service_tracker',
    version='1.0',
    description='Система обліку технічного обслуговування автомобілів',
    author='MaksLord2',
    py_modules=['lab1', 'test_lab3'],  # ім’я .py файлу без розширення
    entry_points={
        'console_scripts': [
            'car-service-tracker = lab1:main',
            'tests = test_lab3:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
