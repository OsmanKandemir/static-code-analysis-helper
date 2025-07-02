from setuptools import setup, find_packages
import os

HERE = os.path.abspath(os.path.dirname(__file__))
DESCRIPTION = 'Static Code Analysis Helper helps you perform static code analysis.'

# README dosyasını uzun açıklama olarak oku
with open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="StaticCodeAnalysisHelper",
    version="1.0.0",
    author="OsmanKandemir",
    author_email="osmankandemir00[@]gmail[.]com",
    license='GPL-3.0',
    url='https://github.com/OsmanKandemir/static-code-analysis-helper.git',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'SAST', 'IAST', 'security-tools'],
    classifiers=[
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Environment :: Console",
        "Topic :: Security",
        "Typing :: Typed",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Telecommunications Industry",
        "Intended Audience :: System Administrators"
    ],
    python_requires='>=3.11',
)