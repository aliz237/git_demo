import argparse

land_cover_classes = [0, 1, 5, 60, 100]

def f(path):
    with open(path) as fin:
        lines = fin.readlines()
    print(f'file {path} has {len(lines)} lines.')
    unique_counts = len(set([int(line) for line in lines
                             if int(line) in land_cover_classes]))
    print(f'{unique_counts} of the desired landcover classes are in {path}')

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("--file_name", "-f",  help="input file name to be line counted")
    args = p.parse_args()
    f(args.file_name)
