import argparse

def menu():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='Location of the text file to load.', required=True)
    parser.add_argument('-o', '--output_file', help='Where the output file should go.', required=True)
    args = parser.parse_args()
    return getattr(args, "file"), getattr(args, "output_file")
