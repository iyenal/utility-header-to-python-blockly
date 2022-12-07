# Gen7 Engine Python3 utility to convert a C/C++ header to a Python comprehensible form
    
import re

# initializing string

txt = open("utilities/header-list.h", "r").read()

txt = txt.replace("}", "} ;")
txt = txt.replace("//{", "")
txt = txt.replace("){", " ) ")
txt = re.sub('{[^}]+}', '', txt)
txt = txt.replace("(", " ")
txt = txt.replace(")", " ")
txt = txt.replace(",", " ")
txt = txt.replace("char *", "str ")
txt = txt.replace("char*", "str")
txt = txt.replace("static ", "")

    
# printing original string 
print ("-----------The original signature : \n" +  txt) 
    
# using split() 
# to extract words from string 
res = txt.split()

function_name = ""
function_param = []
function_types = []

_fname = 0
_ftype = 0
_fparam = 0

output = ""

def reset_code_line():
    global function_name
    global function_param
    global function_types
    
    function_name = ""
    function_param = []
    function_types = []
    _fname = 0
    _ftype = 0
    _fparam = 0

def generate_code_line():
    global output
    global function_name
    global function_param
    global function_types
    
    print(function_name)
    print(function_param)
    print(function_types)

    
    # def createObjectwithRotation(x: float, y: float, z: float, rotX: float, rotY: float, rotZ: float, type: int, name: str, asset) -> None:
    code_line = "def "+function_name+"("
    
    for i in range(0, len(function_param)):
        #print(i)
        code_line = code_line+function_param[i]+": "+function_types[i]+", "
    
    code_line=code_line+"):\n"
    code_line=code_line.replace(", )",")")
    code_line=code_line+"\tpass\n"
    print(code_line)
    output = output + code_line
    
    
# printing result 
print ("\n---------The words :")

for i in res:
    
    #print(i)
    
    # Reset new method
    if(i == ";"):
        print("----New method")
        generate_code_line()
        _fname = 0
        continue
        
    # Get function signature type
    if(_fname == 0):
        _fname = 1
        continue
    # Get function signature name
    if(_fname == 1):
        function_name = i
        _fname = 2
        continue
        
    # Get function param type
    if(_ftype == 0):
        function_types.append(i)
        _ftype = 1
        _fparam = 1
        continue
        
    # Get function param name
    if(_fparam == 1):
        function_param.append(i)
        _ftype = 0
        _fparam = 0
        continue
    
    
print("--------------------- EXPORTED ---------------------")
print("\n")
print(output)