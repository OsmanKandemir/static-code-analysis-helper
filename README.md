![Logo](logo.png)


[![Static-Code-Analysis-Helper](https://img.shields.io/badge/SCA-Helper-red)](https://www.github.com/OsmanKandemir/static-code-analysis-helper)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/OsmanKandemir/static-code-analysis-helper)
[![License](https://img.shields.io/badge/license-GPL-blue.svg)](https://github.com/OsmanKandemir/static-code-analysis-helper/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.10-green)](https://www.python.org)
[![Docker](https://img.shields.io/badge/docker-build-important.svg?logo=Docker)](https://www.docker.com)


# Static-Code-Analysis-Helper

## Description

It detects functions that are likely to cause attack methodologies in many web programming languages ​​and frameworks in your project folder.

#### Helps you perform static code analysis.

Note : Many of the functions described here may not cause vulnerabilities.

## ScreenShot

![](screen.png)


## Programming Languages

- [x] Go
- [x] Python
- [x] Ruby
- [x] PHP
- [x] JavaScript
- [x] Java
- [x] Rust
- [x] Perl
- [x] Ruby on Rails
- [x] Swift
- [x] Golang
- [x] Scala
- [x] Kotlin
- [x] Julia
- [x] Dart
- [x] ASP.NET Core

#### Types of attacks related to results

SQLi, XSS, XXE, CSRF, SSTI, SSRF, IDOR, CORS, XSHM, LFI, DoS, DDoS, RFI, Weak Encryption / Insecure Cryptographic Storage, Path Traversel, Session Attacks,Open Redirect, Insecure File Permissions, XPath Injection, File Uploads, Memory Corruption / Buffer Overflow, Security Misconfiguration, Reflected File Download, CSV Injection, Command Injection, WebSocket Vulnerabilities, Race Condition, Code Injection, Malicious File Deserialization, JWT Vulnerabilities, Broken Access Control, Content Spoofing, Authentication Vulnerabilities, Cookie Vulnerabilities, Business Logic Vulnerabilities.


## TODO

- [ ] ******** Private Repository
- [ ] ******** Private Repository
- [ ] Scan Multiple Programming Language with MultiThread
- [ ] Feature to download from Github, Gitlab or Bitbucket to the repository periodically.



#### NOTE : Please See; [USAGE_POLICY.md](USAGE_POLICY.md) [LICENSE](LICENSE)

## Installation

### From Git

```

git clone https://github.com/OsmanKandemir/static-code-analysis-helper.git
cd static-code-analysis-helper
python3 scanner.py -f "/Users/Test/ProjectFolder" -o result.txt

```

### From Source Code

```
git clone https://github.com/OsmanKandemir/static-code-analysis-helper.git
cd static-code-analysis-helper
python -m build
python setup.py install
```

### From Pypi

The application is [available on PyPI](https://pypi.org/project/StaticCodeAnalysisHelper/). To install with pip:
```
pip install StaticCodeAnalysisHelper

```
### Function Usage

```
from StaticCodeAnalysisHelper import FileScan

# Specific Programming Language Scan

FileScan.AdvancedFileScanning("/Desktop/My-Project","java","result.txt")

# Full Scan

FileScan.AdvancedFileScanning("/Desktop/My-Project",None,"result.txt")

```

### From Dockerfile

```
docker build -t staticcodeanalysishelper .
docker run -v <YOUR-PROJECT-PATH-FOLDER>:/static-code-analysis-helper/Project staticcodeanalysishelper -f /static-code-analysis-helper/Project -p <YOUR-PROGRAMMING-LANGUAGE>
```

### From DockerHub

```
docker pull osmankandemir/staticcodeanalysishelper:v1.0.0
docker run -v <YOUR-PROJECT-PATH-FOLDER>:/static-code-analysis-helper/Project osmankandemir/staticcodeanalysishelper:v1.0.0 -f /static-code-analysis-helper/Project -p <YOUR-PROGRAMMING-LANGUAGE>
```

## Usage

```

-f FOLDER [FOLDER], --folder Folder [FOLDER] Project Folder Path. --folder
-p PROGRAMMING [PROGRAMMING], --programming python [PROGRAMMING] Select Programming Language. --programming
-o OUTPUT [FILENAME] --output [FILENAME] Save output. --output

Programming Language List : java, asp.net, python, dart, ruby, go, php, rust, javascript, perl, scala, golang, kotlin, julia

Please, scan the only project files for the correct result.

```


## Development and Contribution

To continue developing the application **StaticCodeAnalysisHelper/LanguagesFunctions.py** you can add new functions to the file according to the following syntaxes.

```
{"function": "function()","description": "description"}
{"function": "function[]","description": "description"}
{"function": "function","description": "description"}
```

#### See; [CONTRIBUTING.md](CONTRIBUTING.md)


## License

Copyright (c) 2025 Osman Kandemir \
Licensed under the GPL-3.0 License.

## Donations

If you like Static-Code-Analysis-Helper and would like to show support, you can use **Buy A Coffee** or **Github Sponsors** feature for the developer using the button below.

Or

Sponsor me : https://github.com/sponsors/OsmanKandemir 😊

<a href="https://www.buymeacoffee.com/OsmanKandemir" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Your support will be much appreciated😊
