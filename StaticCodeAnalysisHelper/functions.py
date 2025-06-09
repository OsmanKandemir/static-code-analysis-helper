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

from .log import msg
import sys

def AllFunctionsMerge() -> list:

    try:
        all_functions = []
        for i in PythonProgramming():all_functions.append(i)
        for i in JavaProgramming():all_functions.append(i)
        for i in GoProgramming():all_functions.append(i)
        for i in RubyProgramming():all_functions.append(i)
        for i in PhpPrograming():all_functions.append(i)
        for i in JavaScriptProgramming():all_functions.append(i)
        for i in ASPDotNetCoreProgrammingLanguage():all_functions.append(i)
        for i in RustProgrammingLanguage():all_functions.append(i)
        for i in PerlProgrammingLanguage():all_functions.append(i)
        for i in SwiftProgrammingLanguage():all_functions.append(i)
        for i in GolangProgrammingLanguage():all_functions.append(i)
        for i in ScalaProgrammingLanguage():all_functions.append(i)
        for i in KotlinProgrammingLanguage():all_functions.append(i)
        for i in JuliaProgrammingLanguage():all_functions.append(i)
        for i in DartProgrammingLanguage():all_functions.append(i)
        return all_functions
    
    except Exception as Error:
        msg(f"An Error Occurred: {Error}")
        sys.exit()

    
    return all_functions

def AllFunctions() -> list:
    try:
        unique_functions = []
        seen_functions = set()
        for i in AllFunctionsMerge():
                func = i["function"]
                if func not in seen_functions:
                    seen_functions.add(func)
                    unique_functions.append({"function": func, "description": i["description"]})
        return unique_functions
    except Exception as Error:
        msg(f"An Error Occurred: {Error}")
        sys.exit()
