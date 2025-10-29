
from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool
def hello(name: str = "World") -> str:
    return f"Hello {name} from poc-mcp-hello!"


if __name__ == "__main__":
    mcp.run(
        host='0.0.0.0',
        port=8000,
        path='/mcp',
        transport='http'
    )
