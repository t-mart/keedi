import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

import keedi


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_suite = True
        # paths to scan and options for pytest
        self.test_args = ['--verbose', './keedi', './tests']

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))

def extract_email(s):
    """Extract an email from a string like:
    'John Doe <john@doe.com>'
    """
    return s[s.rindex('<'):-1]

install_requires = [
    'numpy',
    'click'
]

tests_require = [
    'mock',
    'pytest',
    'pytest-cov',
]

setup(
        name='keedi',
        version=keedi.__version__,
        packages=['keedi'],
        url='https://github.com/t-mart/keedi',
        license=keedi.__license__,
        description="keedi (Key Distance) quantifies how words are typed on "
                    "keyboard.",
        author=keedi.__author__,
        author_email=extract_email(keedi.__author__),
        entry_points={
            'console_scripts': [
                'keedi = keedi.__main__:main'
            ]
        },
        install_requires=install_requires,
        tests_require=tests_require,
        cmdclass={'test': PyTest},
)
