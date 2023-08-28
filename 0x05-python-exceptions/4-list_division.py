#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    f = 0
    new = [0] * list_length
    for i in range(max(len(my_list_1), len(my_list_2))):
        try:
            res = my_list_1[i] / my_list_2[i]
            new[i] = res
        except ZeroDivisionError:
            print("division by 0")
            f = 1
        except ValueError:
            print("wrong type")
            f = 1
        except IndexError:
            print("out of range")
            f = 1
        finally:
            if f == 1:
                new[i] = 0
    return new
