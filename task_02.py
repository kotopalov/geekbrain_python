def show_data(fname, sname, year_bithday, sity, email='', phone=''):
    print(fname, sname, year_bithday, sity, email, phone)

print("Вариант 1")

show_data("Alex", "First", "1998", "Moscow", 'qwe@qwe.com', '1234567788')
show_data("Ted", "First", "1970", "Moscow")
show_data(fname="Jo", sname="Second", year_bithday="1998", sity="Moscow", email='qwe@qwe.com', phone='1234567788')
show_data(sity="Moscow", year_bithday="1998", fname="Tom", sname="Second", email='qwe@qwe.com', phone='1234567788')
show_data(sity="Moscow", fname="Jim", sname="Do", year_bithday="1981")


def show_data2(**kwargs):
    #init

    d = {
        "fname": "",
        "sname": "",
        "year_bithday": "",
        "sity": "",
        "email": "",
        "phone": ""
    }

    for key, value in kwargs.items():
        if key in d.keys():
            d[key] = value
        else:
            print("Передан лишний аргумент")

    print(" ".join(list(d.values())))


print("\nВариант 2")
show_data2(fname="Jo", sname="Second", year_bithday="1998", sity="Moscow", email='qwe@qwe.com', phone='1234567788')
show_data2(sity="Moscow", year_bithday="1998", fname="Tom", sname="Second", email='qwe@qwe.com', phone='1234567788')
show_data2(sity="Moscow", fname="Jim", sname="Do", year_bithday="1981")
