#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quotient = 0
    new = []
    for i in range(0, list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            new.append(quotient)
    return new
