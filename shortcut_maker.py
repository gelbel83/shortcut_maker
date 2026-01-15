import os, winshell

paths = {}

with open("paths.txt", 'r') as paths_file:
    for path in paths_file:
        key, value = path.split('=')
        paths[key.strip()] = value.strip() 

input_directory = paths['input_directory']
output_directory = paths['output_directory']

extensions = ('.exe')

print('Input directory: ', input_directory)
print('Output directory: ', output_directory)
print()

if not os.path.exists(input_directory) or not os.path.isdir(input_directory):
    print('Invalid input directory')
    exit()

if not os.path.exists(output_directory) or not os.path.isdir(output_directory):
    print('Invalid output directory')
    exit()

for subdirectory, directories, files in os.walk(input_directory):
    for file_name in files:
        if file_name.endswith(extensions):
            _, extension = os.path.splitext(file_name)
            extension = extension.lower()

            print('Directory: ', os.path.relpath(subdirectory, input_directory))
            print('File name: ', file_name)

            try:
                if input('Do you want to make a shorcut(y/n): ') != 'y':
                    print()
                    continue
            except KeyboardInterrupt:
                print('\nInput interrupted')
                exit()

            try:
                shortcut_name = input('Shortcut name(default: ' + file_name[:-len(extension)] + '): ') or file_name[:-len(extension)]
            except KeyboardInterrupt:
                print('\nInput interrupted')
                exit()

            shortcut_path = os.path.join(output_directory, shortcut_name + '.lnk')

            try:
                with winshell.shortcut(shortcut_path) as shortcut:
                    shortcut.path = os.path.join(subdirectory, file_name)
            except:
                print('There was an error with creating the shortcut')

            print()