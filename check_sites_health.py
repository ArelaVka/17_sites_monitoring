def load_urls4check(path):
    try:
        check_list = open(path, 'r')
        return check_list
    except ValueError:
        return False


def is_server_respond_with_200(url):
    pass

def get_domain_expiration_date(domain_name):
    pass

if __name__ == '__main__':
    pass
