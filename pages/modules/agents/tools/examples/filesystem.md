

文件系统工具[#](#file-system-tools "本标题的永久链接")
========================================

LangChain提供了与本地文件系统交互的工具。本笔记本演示了其中的一些。

注意：这些工具不建议在沙盒环境之外使用！

首先，我们将导入工具。

```
from langchain.tools.file_management import (
    ReadFileTool,
    CopyFileTool,
    DeleteFileTool,
    MoveFileTool,
    WriteFileTool,
    ListDirectoryTool,
)
from langchain.agents.agent_toolkits import FileManagementToolkit
from tempfile import TemporaryDirectory

# We'll make a temporary directory to avoid clutter
working_directory = TemporaryDirectory()

```

文件管理工具包[#](#the-filemanagementtoolkit "本标题的永久链接")
-------------------------------------------------

如果您想为代理提供所有文件工具，使用工具包很容易。我们将临时目录作为根目录传递给LLM作为工作区。

建议始终传递根目录，因为没有根目录，LLM很容易污染工作目录，没有根目录，也没有验证可以防止简单的提示注入。

```
toolkit = FileManagementToolkit(root_dir=str(working_directory.name)) # If you don't provide a root_dir, operations will default to the current working directory
toolkit.get_tools()

```

```
[CopyFileTool(name='copy_file', description='Create a copy of a file in a specified location', args_schema=<class 'langchain.tools.file_management.copy.FileCopyInput'>, return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x1156f4350>, root_dir='/var/folders/gf/6rnp_mbx5914kx7qmmh7xzmw0000gn/T/tmpxb8c3aug'),
 DeleteFileTool(name='file_delete', description='Delete a file', args_schema=<class 'langchain.tools.file_management.delete.FileDeleteInput'>, return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x1156f4350>, root_dir='/var/folders/gf/6rnp_mbx5914kx7qmmh7xzmw0000gn/T/tmpxb8c3aug'),
 FileSearchTool(name='file_search', description='Recursively search for files in a subdirectory that match the regex pattern', args_schema=<class 'langchain.tools.file_management.file_search.FileSearchInput'>, return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x1156f4350>, root_dir='/var/folders/gf/6rnp_mbx5914kx7qmmh7xzmw0000gn/T/tmpxb8c3aug'),
 MoveFileTool(name='move_file', description='Move or rename a file from one location to another', args_schema=<class 'langchain.tools.file_management.move.FileMoveInput'>, return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x1156f4350>, root_dir='/var/folders/gf/6rnp_mbx5914kx7qmmh7xzmw0000gn/T/tmpxb8c3aug'),
 ReadFileTool(name='read_file', description='Read file from disk', args_schema=<class 'langchain.tools.file_management.read.ReadFileInput'>, return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x1156f4350>, root_dir='/var/folders/gf/6rnp_mbx5914kx7qmmh7xzmw0000gn/T/tmpxb8c3aug'),
 WriteFileTool(name='write_file', description='Write file to disk', args_schema=<class 'langchain.tools.file_management.write.WriteFileInput'>, return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x1156f4350>, root_dir='/var/folders/gf/6rnp_mbx5914kx7qmmh7xzmw0000gn/T/tmpxb8c3aug'),
 ListDirectoryTool(name='list_directory', description='List files and directories in a specified folder', args_schema=<class 'langchain.tools.file_management.list_dir.DirectoryListingInput'>, return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x1156f4350>, root_dir='/var/folders/gf/6rnp_mbx5914kx7qmmh7xzmw0000gn/T/tmpxb8c3aug')]

```

### 选择文件系统工具[#](#selecting-file-system-tools "本标题的永久链接")

如果您只想选择某些工具，在初始化工具包时可以将它们作为参数传递，或者您可以单独初始化所需的工具。

```
tools = FileManagementToolkit(root_dir=str(working_directory.name), selected_tools=["read_file", "write_file", "list_directory"]).get_tools()
tools

```

```
[ReadFileTool(name='read_file', description='Read file from disk', args_schema=<class 'langchain.tools.file_management.read.ReadFileInput'>, return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x1156f4350>, root_dir='/var/folders/gf/6rnp_mbx5914kx7qmmh7xzmw0000gn/T/tmpxb8c3aug'),
 WriteFileTool(name='write_file', description='Write file to disk', args_schema=<class 'langchain.tools.file_management.write.WriteFileInput'>, return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x1156f4350>, root_dir='/var/folders/gf/6rnp_mbx5914kx7qmmh7xzmw0000gn/T/tmpxb8c3aug'),
 ListDirectoryTool(name='list_directory', description='List files and directories in a specified folder', args_schema=<class 'langchain.tools.file_management.list_dir.DirectoryListingInput'>, return_direct=False, verbose=False, callback_manager=<langchain.callbacks.shared.SharedCallbackManager object at 0x1156f4350>, root_dir='/var/folders/gf/6rnp_mbx5914kx7qmmh7xzmw0000gn/T/tmpxb8c3aug')]

```

```
read_tool, write_tool, list_tool = tools
write_tool.run({"file_path": "example.txt", "text": "Hello World!"})

```

```
'File written successfully to example.txt.'

```

```
# List files in the working directory
list_tool.run({})

```

```
'example.txt'

```

