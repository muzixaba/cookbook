from pathlib import Path
import os

# Get working directory
print(os.getcwd())
print(Path.cwd())

# Create a path from string
os.path.join("test_folder", "sample.txt")

# Creating a path with string with path
Path('test_folder/sample2.txt')

# Create path using forward slash to join path
Path('test_folder') / 'sample2.txt'

# Create path using JoinPath
Path().joinpath('test_folder', 'sample.txt')

# Create path using joinpath for full path
Path.home().joinpath('test_folder', 'sample.txt')

# Get to home directory with os.path
os.path.expanduser("~")

# Get to home directory with os
# os.environ["HOME"]

# Get to home directory with Path
Path.home()
Path('~').expanduser()

# Get absolute path with os
os.path.abspath('test_folder/sample.txt')

# Get relative path with Path
Path('test_folder/sample.txt').resolve()

# Get absolute path with Path
Path('test_folder/sample.txt').absolute()

# Get components of a Path
os_path = os.path.join("test_folder", "sample.txt")
p_path = Path("test_folder") / "sample.txt"

# Get name of file with Path
p_path.name

# Get name of file with os
os.path.basename(os_path)

# Get parent directory name
p_path.parent
