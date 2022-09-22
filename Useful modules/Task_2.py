"""
Написать функцию host_range_ping() (возможности которой основаны на функции из примера 1)
для перебора ip-адресов из заданного диапазона. Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""

from Task_1 import check_is_ipaddress, host_ping


def host_range_ping(get_list=False):
    while True:
        start_ip = input("Введите первоначальный адрес: ")  # запрос первоначального адреса
        try:
            ipv4_start = check_is_ipaddress(start_ip)
            last_oct = int(start_ip.split('.')[3])       # смотрим чему равен последний октет
            break
        except Exception as e:
            print(e)
    while True:
        end_ip = input("Сколько адресов проверить?: ")  # Запрос на количество проверяемых адресов
        if not end_ip.isnumeric():
            print("Необходимо ввести число")
        else:
            if (last_oct + int(end_ip)) > 255+1:  # По условию меняется только последний октет
                print(f"Можем менять только последний октет, "
                      f"т.е. максимальное число хостов {255+1 - last_oct}")
            else:
                break
    host_list = []
    [host_list.append(str(ipv4_start + x)) for x in range(int(end_ip))]  # формируем список ip
    if not get_list:   # передаём список в функцию из задания #1 для проверки
        host_ping(host_list)
    else:
        return host_ping(host_list, True)


if __name__ == "__main__":
    host_range_ping()
