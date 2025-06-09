import sys, os, re 
from .LanguagesFunctions import (
                                PythonProgramming,
                                JavaProgramming,
                                GoProgramming,
                                RubyProgramming,
                                PhpPrograming,
                                JavaScriptProgramming,
                                ASPDotNetCoreProgrammingLanguage,
                                RustProgrammingLanguage,
                                PerlProgrammingLanguage,
                                SwiftProgrammingLanguage,
                                GolangProgrammingLanguage,
                                ScalaProgrammingLanguage,
                                KotlinProgrammingLanguage,
                                JuliaProgrammingLanguage,
                                DartProgrammingLanguage
                                )
from .functions import AllFunctions
from .log import msg,bcolors

class AdvancedFileScanning:
    def __init__(self,path,programming,output) -> None:
        self.path_ = path
        self.programming_ = programming
        self.output_ = output

        if self.programming_ == None:
            for i in AllFunctions():self.FindVulnFunc(i["function"],i["description"])
        if self.programming_ == "python":
            for i in PythonProgramming():self.FindVulnFunc(i["function"],i["description"])
        if self.programming_ == "java":
            for i in JavaProgramming():self.FindVulnFunc(i["function"],i["description"])
        if self.programming_ == "go":
            for i in GoProgramming():self.FindVulnFunc(i["function"],i["description"])    
        if self.programming_ == "ruby":
            for i in RubyProgramming():self.FindVulnFunc(i["function"],i["description"])  
        if self.programming_ == "php":
            for i in PhpPrograming():self.FindVulnFunc(i["function"],i["description"])  
        if self.programming_ == "javascript":
            for i in JavaScriptProgramming():self.FindVulnFunc(i["function"],i["description"])  
        if self.programming_ == "asp.net":
            for i in ASPDotNetCoreProgrammingLanguage():self.FindVulnFunc(i["function"],i["description"])  
        if self.programming_ == "rust":
            for i in RustProgrammingLanguage():self.FindVulnFunc(i["function"],i["description"])  
        if self.programming_ == "perl":
            for i in PerlProgrammingLanguage():self.FindVulnFunc(i["function"],i["description"])      
        if self.programming_ == "swift":
            for i in SwiftProgrammingLanguage():self.FindVulnFunc(i["function"],i["description"])    
        if self.programming_ == "golang":
            for i in GolangProgrammingLanguage():self.FindVulnFunc(i["function"],i["description"])    
        if self.programming_ == "scala":
            for i in ScalaProgrammingLanguage():self.FindVulnFunc(i["function"],i["description"])   
        if self.programming_ == "kotlin":
            for i in KotlinProgrammingLanguage():self.FindVulnFunc(i["function"],i["description"]) 
        if self.programming_ == "julia":
            for i in JuliaProgrammingLanguage():self.FindVulnFunc(i["function"],i["description"]) 
        if self.programming_ == "dart":
            for i in DartProgrammingLanguage():self.FindVulnFunc(i["function"],i["description"]) 

    def FindVulnFunc(self,FunctionName,Description):
        for root, dirs, files in os.walk(self.path_):
            for file in files:
                folder_path = os.path.join(root, file)
                try:
                    with open(folder_path, 'r', encoding='utf-8', errors='ignore') as f:
                        count = 1
                        pattern = rf'({re.escape(FunctionName.split("()")[0])}\(\s*.*?\s*\)|' \
                                  rf'{re.escape(FunctionName.split("[]")[0])}\[\s*.*?\s*\]|' \
                                  rf'{re.escape(FunctionName)})'
                        for satir in f:
                            if re.search(pattern, satir):
                                msg(f"{bcolors.YELLOW}'{FunctionName}'{bcolors.ENDC} function was found. {bcolors.LOG}{Description}{bcolors.ENDC} - Path: {bcolors.OKGREEN}{folder_path},{bcolors.ENDC}  {bcolors.LOG}{count}. Line{bcolors.ENDC}")
                                if self.output_:
                                    with open(f"{self.output_}", "a+") as f:
                                        f.write(f"'{FunctionName}()' function was found. {Description} - Path: {folder_path}, {count}. Line \n")
                                else:
                                    pass
                            count += 1
                except UnicodeDecodeError:
                    msg(f"File not read (UnicodeDecodeError): {folder_path}")
                    sys.exit()
                except FileNotFoundError:
                    msg(f"File not found: {folder_path}")
                    sys.exit()

    @property
    def path(self) -> str:
        return self.path_
    
    @property
    def programming(self) -> str:
        return self.programming_
    
    
    def __str__(self):
        return f"StaticCodeAnalysisHelper"

    def __repr__(self):
        return 'StaticCodeAnalysisHelper(path_=' + str(self.path_) + ',programming_='+str(self.programming_)



if __name__ == "__main__":
    sys.exit()