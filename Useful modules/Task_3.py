"""
Написать функцию host_range_ping() (возможности которой основаны на функции из примера 1)
для перебора ip-адресов из заданного диапазона. Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""

from tabulate import tabulate
from Task_2 import host_range_ping


def host_range_ping_tab():
    res_dict = host_range_ping(True)
    print()
    print(tabulate([res_dict], headers='keys', tablefmt='pipe', stralign='center'))


if __name__ == "__main__":
    host_range_ping_tab()
