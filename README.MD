## Shortcut Maker
A CLI tool for automating the process of creating many shortcuts on windows   
Good for making shortcuts to multiple programs that were installed without a wizard   

### How to use: 
Enter the input and output directories in ```paths.txt```   
For example something like: 
```
input_directory=C:\path\to\the\folder\with\my\programs
output_directory=C:\path\to\the\start\menu
```
Install the necessary modules with [pip](https://pypi.org/project/pip/)
```
pip install pywin32
```
Run shortcut_maker.py with your respective version of [python](https://www.python.org/):
```
py shortcut_maker.py
```
**Remember that if the input or the output directory are protected by admin rights you have tu run the file as an administrator!**