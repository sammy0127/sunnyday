from setuptools import setup

setup(
    name=['sunnyday'],
    package=['sunnyday'],
    version='1.0.0',
    license='MIT',
    description='Weather Forecast Data',
    author='Sam Eads',
    author_email='sam@unusualconsultants.com',
    url='www.unusualconsultants.com',
    keywords=['weather', 'forecast', 'openweather'],
    install_requires=['requests',
                      ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
