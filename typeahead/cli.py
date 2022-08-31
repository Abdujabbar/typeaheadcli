import argparse


def parse():
    parser = argparse.ArgumentParser(description='Please enter inputs')
    parser.add_argument('data_path', metavar='data_path',
                        type=str, help='Path to data source')

    return parser.parse_args()
