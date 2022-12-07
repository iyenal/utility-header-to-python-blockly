# Gen7 Engine Python3 utility to convert a C/C++ header to a Blockly toolkit
    
import re

# initializing string

txt = open("header-list.h", "r").read()

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

function_typedef = ""
function_name = ""
function_param = []
function_types = []

_fname = 0
_ftype = 0
_fparam = 0

output = ""
xml = ""

def reset_blocks_line():
    global function_typedef
    global function_name
    global function_param
    global function_types
    
    function_typedef = ""
    function_name = ""
    function_param = []
    function_types = []
    _fname = 0
    _ftype = 0
    _fparam = 0

def generate_blocks_line():
    global output
    global xml
    global function_typedef
    global function_name
    global function_param
    global function_types
    
    print(function_name)
    print(function_param)
    print(function_types)

    
    """
    Blockly.Blocks['createObjectWithRotationScale'] = { init: function() { this.appendDummyInput().appendField("createObjectWithRotationScale");

    this.appendValueInput('posX').setCheck('Number').appendField('posX');
    this.appendValueInput("posY").setCheck("Number").appendField("posY");
    this.appendValueInput("filename").setCheck("String").appendField("Filename");

    this.appendDummyInput();this.setPreviousStatement(true, null);this.setNextStatement(true, null);this.setColour(230);this.setTooltip("");this.setHelpUrl("");}};
    """
    
    # -------------------- Blockly Block
    
    # Function declaration
    blocks_line = "Blockly.Blocks['"+function_name+"'] = { init: function() { this.appendDummyInput().appendField('"+function_name+"');\n"
    
    # Function Body
    for i in range(0, len(function_param)):
        
        # Number
        if(function_types[i] == "int" or function_types[i] == "float"):
            blocks_line += "\tthis.appendValueInput('"+function_param[i]+"').setCheck('Number').appendField('"+function_param[i]+"');\n"
        # String
        if(function_types[i] == "str"):
            blocks_line += "\tthis.appendValueInput('"+function_param[i]+"').setCheck('String').appendField('"+function_param[i]+"');\n"
      
    # Function end
    if(len(function_param) > 0):
        blocks_line+="this.appendDummyInput();"
        
    if(function_typedef == "bool"):
        blocks_line+="this.setOutput(true, 'Boolean');this.setColour(330);this.setTooltip('');this.setHelpUrl('');}};\n"
    elif(function_typedef == "str"):
        blocks_line+="this.setOutput(true, 'String');this.setColour(330);this.setTooltip('');this.setHelpUrl('');}};\n"
    elif(function_typedef == "float"):
        blocks_line+="this.setOutput(true, 'Number');this.setColour(330);this.setTooltip('');this.setHelpUrl('');}};\n"
    elif(function_typedef == "int"):
        blocks_line+="this.setOutput(true, 'Number');this.setColour(330);this.setTooltip('');this.setHelpUrl('');}};\n"
    elif(function_typedef == "void"):
        blocks_line+="this.setPreviousStatement(true, null);this.setNextStatement(true, null);this.setColour(230);this.setTooltip('');this.setHelpUrl('');}};\n"
    blocks_line+="\n"
    
    # ------------------- Blockly Generator
    
    """
    Blockly.Python['createObjectWithRotationScale'] = function(block) {

      var posX = Blockly.Python.valueToCode(block, 'posX', Blockly.Python.ORDER_ATOMIC);
      var posY = Blockly.Python.valueToCode(block, 'posY', Blockly.Python.ORDER_ATOMIC);
      var filename = Blockly.Python.valueToCode(block, 'filename', Blockly.Python.ORDER_ATOMIC);

      var code = 'createObjectWithRotationScale('+posX+','+posY+','+filename+')\n';

    return code;};
    """
    
    # Function declaration
    blocks_line += "Blockly.Python['"+function_name+"'] = function(block) {\n"
    
    # Function Body
    for i in range(0, len(function_param)):
        
        blocks_line += "\tvar "+function_param[i]+" = Blockly.Python.valueToCode(block, '"+function_param[i]+"', Blockly.Python.ORDER_ATOMIC);\n"
      
    # Function end
    blocks_line+="\n\tvar code = '"+function_name+"("
    for i in range(0, len(function_param)):
        
        if(i != 0):
            blocks_line += "+','+"
        else:
            blocks_line += "'+"
            
        blocks_line += function_param[i]
        
        if(i == len(function_param)-1):
            blocks_line += "+'"
            
    if(function_typedef == "void"):
        blocks_line+=")\\n';"
        blocks_line+="\nreturn code;};"
    else:
        blocks_line+=")';"
        blocks_line+="\nreturn [code, Blockly.Python.ORDER_NONE];};"
    blocks_line+="\n"
    
    # ------- Add everything
    
    output+=blocks_line
    xml+='\t<block type="'+function_name+'"></block>\n'
    
    print(blocks_line)
    
# printing result 
print ("\n---------The words :")

for i in res:
    
    #print(i)
    
    # Reset new method
    if(i == ";"):
        print("----New method----")
        generate_blocks_line()
        reset_blocks_line()
        _fname = 0
        continue
        
    # Get function signature type
    if(_fname == 0):
        function_typedef = i
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
    
    
print("\n")
print("\n")
print("\n")
print("============================================= EXPORTED ====================================================")
print("\n")
print("BLOCKLY JS:\n")
print("\n")
print(output)
print("\n")
print("BLOCKLY XML:\n")
print("\n")
print(xml)