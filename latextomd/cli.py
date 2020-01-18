import sys


def main():
    if len(sys.argv)==1:
        print('You must enter a source file')
    elif len(sys.argv)==2:
        source_file = sys.argv[1]
        export_file = source_file.replace('.tex','.md')
    else:
        source_file = sys.argv[1]
        export_file = sys.argv[2]

if __name__ == '__main__':
    main()