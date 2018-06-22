import whois
import argparse
import os


def generate_parser():
    parser = argparse.ArgumentParser(
        description='Sites checker')
    parser.add_argument(
        '-f',
        '--file',
        type=str,
        dest='path',
        metavar='<path_to_file>',
        required=True,
        help='full path to file with list of url\'s')
    return parser


def check_parser_arguments(path):
    if path and not os.path.isfile(path):
        parser.error('Wrong path to input file')


def load_urls4check(path):
    try:
        with open(path, 'r') as check_list_file:
            return check_list_file.read()
    except ValueError:
        return False


def is_server_respond_with_200(url):
    pass


def get_domain_expiration_date(domain_name):
    pass


if __name__ == '__main__':
    parser = generate_parser()
    args = parser.parse_args()
    check_list_data = load_urls4check(args.input_file)
    urls = check_list_data.split('\n')


