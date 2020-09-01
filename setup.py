from setuptools import setup

setup(
        name='dailymass',
        version='0.0.1',
        description='daily mass readings',
        py_modules=["main"],
        #package_dir={'': 'src'},
        packages = ["dailymass"],
        entry_points = {
            "console_scripts": ['dailymass = dailymass.dailymass:main']
        },
        setup_requires=['wheel'],
        install_requires=[
            'requests', 
            'beautifulsoup4', 
            'termcolor',
        ],
    )
