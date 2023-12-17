import random
import string


def generate_order_id():
    return f'Order - {random_code()}'


def random_code():
    rand = random.SystemRandom()
    rand_code = rand.choices(string.digits, k=5)
    return ''.join(rand_code)
