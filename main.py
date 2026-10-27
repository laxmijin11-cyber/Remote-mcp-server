# def main() -> None:
#     print("Hello from remote-mcp-server!")

from fastmcp import FastMCP
import random
import json

# Create the FastMCP server instance
mcp = FastMCP("Simple Calculator Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers together.
    Args:
    a: First number
    b: Second Number

    Returns: The sum of a and b
    """
    return a + b


# Tool to generate  arandom number
@mcp.tool()
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """Generate a number within a range.

    Args:
    min_val:Minimum value(default:1)
    max_val:Maximum Value(default:100)

    Returns:
    A random integer between min_value and max_value
    """
    return random.randint(min_val, max_val)


# Resource:Server information
@mcp.resource("info://server")
def server_info() -> str:
    """
    Get information about the server.
    """
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic mcp server with math tools.",
        "tools": ["add", "random_number"],
        "author": "Your name",
    }
    return json.dumps(info, indent=2)


app = mcp.http_app()

# Start the server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

# Problem: json.dump() writes to a file. You want to return a string. Also, it's missing the obj parameter.
# return json.dumps(info, indent=2)
