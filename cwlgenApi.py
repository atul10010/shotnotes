from flask import Flask
from flask import request, jsonify
import cwlgen

app = Flask(__name__)

@app.route("/genCWL", methods=['POST'])
def generateCWL():
    query_parameters = request.form
    print (query_parameters)
    # Create a tool
    cwl_tool = cwlgen.CommandLineTool(tool_id='comm',
                                      label='print lines matching a pattern',
                                      base_command=query_parameters.get('textcom'),cwl_version=query_parameters.get('CWL_Version'))

    # Add 1 input (input file)
    file_binding = cwlgen.CommandLineBinding(position=1)
    input_file = cwlgen.CommandInputParameter('input_file',
                                              param_type=query_parameters.get('textinput'),
                                              input_binding=file_binding,
                                              doc='input file from which you want to look for the pattern')
    cwl_tool.inputs.append(input_file)
    
    # Add 1 output
    output = cwlgen.CommandOutputParameter('output',
                                           param_type=query_parameters.get('textoutput'),
                                           doc='output file ref')
    cwl_tool.outputs.append(output)
   

    # Add documentation
    cwl_tool.doc = "Simple CWL 1 input and one output"

    
    # Write in an output file
    cwl_tool.export(query_parameters.get('textoutname'))

    return '<h2>CWL File generated Successfully</h2>'


if __name__ == '__main__':
    app.run(debug=True)
