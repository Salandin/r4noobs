from setuptools import setup, find_packages

VERSION = '0.2.0'

setup(
    name="mkdocs-windmill-dark",
    version=VERSION,
    url='https://github.com/noraj1337/mkdocs-windmill-dark',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Topic :: Documentation',
        'Topic :: Text Processing',
    ],
    install_requires=[
        'mkdocs',
    ],
    license='MIT',
    description='MkDocs dark theme focused on navigation and usability',
    author='Alexandre ZANNI',
    author_email='alexandre.zanni@engineer.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'windmill-dark = mkdocs_windmill_dark',
        ]
    },
    zip_safe=False
)
