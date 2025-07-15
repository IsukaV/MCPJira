import subprocess
import json
import sys

def call_mcp_tool(tool_name, **params):
    """
    Call an MCP tool via STDIO communication
    """
    # Start the MCP server process
    proc = subprocess.Popen(
        ["python", "test.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    try:
        # Create the tool call request
        request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": params
            }
        }
        
        # Send the request
        request_json = json.dumps(request) + "\n"
        proc.stdin.write(request_json)
        proc.stdin.flush()
        
        # Read the response
        response_line = proc.stdout.readline()
        if response_line:
            response = json.loads(response_line)
            return response
        else:
            return {"error": "No response received"}
            
    except Exception as e:
        return {"error": f"Communication error: {str(e)}"}
    finally:
        # Clean up
        proc.stdin.close()
        proc.terminate()
        proc.wait()

if __name__ == "__main__":
    # Call the greet tool with name "isuka"
    result = call_mcp_tool("greet", name="isuka")
    print("MCP Tool Call Result:")
    print(json.dumps(result, indent=2)) 