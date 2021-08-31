from openapi_server.models.tool import Tool  # noqa: E501
from openapi_server.models.tool_dependencies import ToolDependencies  # noqa: E501
from openapi_server.models.tool_type import ToolType  # noqa: E501
from openapi_server.models.license import License


def get_tool():  # noqa: E501
    """Get tool information

    Get information about the tool # noqa: E501


    :rtype: Tool
    """
    tool = Tool(
        name="connor-phi-annotator",
        version="0.0.4",
        license=License.APACHE_2_0,
        repository="github:cascadianblue/phi-annotator",
        description="Connor Boyle's PHI annotator based on a linear SVM.",
        author="Connor Boyle",
        author_email="connor.bo@gmail.com",
        url="https://github.com/cascadianblue/phi-annotator",
        type=ToolType.PHI_ANNOTATOR,
        api_version="1.2.0"
    )
    return tool, 200


def get_tool_dependencies():  # noqa: E501
    """Get tool dependencies

    Get the dependencies of this tool # noqa: E501


    :rtype: ToolDependencies
    """
    return ToolDependencies(tools=[]), 200
