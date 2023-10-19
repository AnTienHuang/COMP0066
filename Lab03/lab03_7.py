import sys

file_list = sys.argv[1:]

for file in file_list:
    try:
        with open(f"{file}", 'r') as fp:
            lines = len(fp.readlines())
            print(f'Total Number of lines in {file}:', lines)
    except Exception as e:
        print(f'Failed to read file {file}:', e)
