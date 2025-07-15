import subprocess
import json
import time

def call_mcp_greet(name):
    """
    Call the greet tool in the MCP server with the given name
    """
    # Start the MCP server
    proc = subprocess.Popen(
        ["python", "test.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    try:
        # Wait a moment for the server to start
        time.sleep(0.5)
        
        # Create the tool call request
        request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": "greet",
                "arguments": {
                    "name": name
                }
            }
        }
        
        # Send the request
        request_json = json.dumps(request) + "\n"
        print(f"Sending request: {request_json.strip()}")
        
        proc.stdin.write(request_json)
        proc.stdin.flush()
        
        # Read the response
        response_line = proc.stdout.readline()
        if response_line:
            response = json.loads(response_line)
            print(f"Received response: {json.dumps(response, indent=2)}")
            return response
        else:
            print("No response received")
            return None
            
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        # Clean up
        proc.stdin.close()
        proc.terminate()
        proc.wait()

if __name__ == "__main__":
    print("Calling greet tool with name 'isuka'...")
    result = call_mcp_greet("isuka")
    
    if result and "result" in result:
        print(f"\n🎉 Greeting: {result['result']}")
    else:
        print("❌ Failed to get greeting") 