import string
from random import choices


def random_string(length):
    return ''.join(choices(
        string.ascii_letters +
        ' ' +
        string.digits,
        k=length
    ))
