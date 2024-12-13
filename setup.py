from setuptools import setup

requires = ["flake8>3.0.0"]
setup(
    name='flake8-russian-comments',
    version='1.0',
    description='A Flake8 plugin to restrict Russian comments',
    author='AusaafNabi',
    author_email='no-reply@example.com',
    url='https://github.com/ausaafnabi/Rulinter',
    py_modules=['_russian_comments_checker','_line_endings'],
    install_requires=requires,
    entry_points={
        'flake8.extension': [
            'RU001 = _russian_comments_checker:RussianCommentsChecker',
            'LE = _line_endings:LineEndingsChecker',
        ],
    },
)

