from fastmcp import FastMCP

mcp = FastMCP("TestServer")

@mcp.tool()
def ping():
    return "pong"

if __name__ == "__main__":
    mcp.run()
