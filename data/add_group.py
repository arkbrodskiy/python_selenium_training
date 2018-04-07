import random
import string
from model.group import Group


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


test_data = [Group(name=random_string('name', 10),
                   header=random_string('header', 20),
                   footer=random_string('footer', 20)),
             Group(name="", header="", footer="")]
