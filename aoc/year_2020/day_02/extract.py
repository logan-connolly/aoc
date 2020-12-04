def extract_passwd_data(passwd_input):
    """Helper for formatting input data"""
    _range, target, passwd = passwd_input.split()
    indices = [int(n) for n in _range.split("-")]
    return indices, target.strip(":"), passwd
