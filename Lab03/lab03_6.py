# units = ("B", "KB", "MB", "GB")

def convert(bytes):    
    kb = bytes / 2 ** 10
    mb = kb / 2 ** 10
    gb = mb / 2 ** 10
    print(f'{bytes} B')
    print(f'{kb} KB')
    print(f'{mb} MB')
    print(f'{gb} GB')

bytes = int(input('Input the number of bytes to be converted: '))
# bytes = 537395200
convert(bytes)
