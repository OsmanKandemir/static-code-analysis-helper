import os,sys,argparse
from StaticCodeAnalysisHelper.log import bcolors,msg
from StaticCodeAnalysisHelper.FileScan import AdvancedFileScanning


def print_des():
    print(rf"""{bcolors.YELLOW}                                                                                    
   _____ __        __  _         ______          __        ___                __           _     
  / ___// /_____ _/ /_(_)____   / ____/___  ____/ /__     /   |  ____  ____ _/ /_  _______(_)____
  \__ \/ __/ __ `/ __/ / ___/  / /   / __ \/ __  / _ \   / /| | / __ \/ __ `/ / / / / ___/ / ___/
 ___/ / /_/ /_/ / /_/ / /__   / /___/ /_/ / /_/ /  __/  / ___ |/ / / / /_/ / / /_/ (__  ) (__  ) 
/____/\__/\__,_/\__/_/\___/   \____/\____/\__,_/\___/  /_/  |_/_/ /_/\__,_/_/\__, /____/_/____/  
                                                                            /____/ Helper v1.0.0           
Author : OsmanKandemir{bcolors.ENDC}
        """)

print_des()


class StaticCodeAnalysisHelperException(Exception):
    """
    StaticCodeAnalysisHelper exception class
    """
    def __init__(self, message):
        """
        StaticCodeAnalysisHelperException class constructor
        :param message: string
        """
        self.message_ = message

        Exception.__init__(self, '%s' % (self.message_))


def STARTS():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--folder", nargs='+', required="True", help="Project folder path. --folder /folder/folder/Project")
    parser.add_argument("-p","--programming", nargs='?' , help="Programming Language. Blank argument is agressive scan. Specific scan sample argument is --programming java")
    parser.add_argument("-o","--output", action = "store", help="Save output. --output result.txt")

    args = parser.parse_args()
    programming = args.programming if args.programming else None
    output = args.output if args.output else None
    if not programming in ["java","asp.net","python","dart","ruby","go","php","rust","javascript","perl","swift","scala","golang","kotlin","julia",None]:
        msg(f"""{bcolors.LOG}ERROR{bcolors.ENDC}{bcolors.HEADER} Unknown Programming Language. You must choose the following programming languages or leave  blank.{bcolors.YELLOW}
                                                                            java
                                                                            asp.net
                                                                            python
                                                                            dart
                                                                            ruby
                                                                            go
                                                                            php
                                                                            rust
                                                                            javascript
                                                                            perl
                                                                            scala
                                                                            golang
                                                                            kotlin
                                                                            julia{bcolors.ENDC}""")
        sys.exit()

    AdvancedFileScanning(args.folder[0],programming,output)

if __name__ == "__main__":
    STARTS()
    sys.exit()