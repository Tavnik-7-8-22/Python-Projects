def sq(x):
    """
    Squares a given number.
    :param x: The number to square (int or float)
    :return: x squared (float)
    """
    return x**2
# Sample output:

print(sq(4))
# Output: 16

print(sq(6))
# Output: 36


def rev_list(a_list):
    """
    Reverses a given list.
    :param a_list: The list to reverse (string)
    :return: Reversed list (string)
    """
    return a_list[::-1]
# Sample output:

print(rev_list([1, 2, 3, 4, 5]))
# Output: [5, 4, 3, 2, 1]

print(rev_list(['z', 'y', 'x', 'w']))
# Output: ['w', 'x', 'y', 'z']

print(rev_list([1, 2, [3,4], 5]))
# Output: [5, [3, 4], 2, 1]


def shift_list(a_list, num):
    """
    Accepts a list and the number of places to shift this list to the left.
    :param a_list: The un-shifted list (string)
    :param num: the number of places to shift this list to the left (int)
    :return: The shifted list (string)
    """
    return (a_list[num::1]+a_list[0:num])
# Sample output:

print(shift_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
# Output: [4, 5, 6, 7, 8, 9, 1, 2, 3]

print(shift_list(['spam', 'I', 'like'], 1))
# Output: ['I', 'like', 'spam']


def check_ends(s):
    '''
    Takes in a string s and returns True if the first character in s is the same as the last character in s, otherwise it returns false.
    :param s: The string that will be checked (string)
    :return: True or False (boolean)
    '''
    return (s[0]==s[-1])
# Sample output:

print(check_ends('no match'))
# Output: False

print(check_ends('hah! a match'))
# Output: True

print(check_ends('q'))
# Output: True

print(check_ends(' '))
# Output: True


def flipside(s):
    """
    Accepts a string s and returns a string whose first half is s's second half and whose second half is s's first half. 
    :param s: The string that will be flipped (string)
    :return: The flipped string (string)
    """
    x = len(s)//2
    return s[x:]+s[:x]
# Sample output:

print(flipside('homework'))
# Output: workhome

print(flipside('carpets'))
# Output: petscar


def convert_from_seconds(seconds):
    """
    Accepts a non-negative integer number of seconds sec and returns a list of four non-negative integers that represents that number of seconds in more conventional units of time
    :param sec: a non-negative integer number of seconds (integer)
    :return: A list of four non-negative integers that represents that number of seconds in more conventional units of time (integer)
    """
    days = seconds // (24*60*60)
    seconds = seconds - days*(24*60*60)
    hours = seconds // (60*60)
    seconds = seconds - hours*(60*60)
    minutes = seconds // 60
    seconds = seconds - minutes*60
    seconds = seconds
    return [days, hours, minutes, seconds]
# Sample output:

print(convert_from_seconds(610))
# Output: [0, 0, 10, 10]

print(convert_from_seconds(100000))
# Output: [1, 3, 46, 40]


def interp(low, hi, fraction):
    """
    Takes in three numbers, low, hi, and fraction, and should return a floating-point value that linearly interpolates between low and hi by the amount specified by fraction.
    :param low: If fraction is zero, low will be returned (integer)
    :param hi: If fraction is one, hi will be returned (integer)
    :param fraction: If fraction is less than zero or greater than one, it will linearly extrapolate (integer) 
    :return: A floating-point value that linearly interpolates between low and hi by the amount specified by fraction (integer)
    """
    return
# Sample output:

print(interp(4.0, 10.0, 0.5))  # half way (.5) from 4.0 to 10.0
# Output: 7.0

print(interp(1.0, 3.0, 0.25))  # a quarter of the way from 1.0 to 3.0
# Output: 1.5

print(interp(2, 12, 0.22))  # 22% of the way from 2 to 12
# Output: 4.2

print(interp(24, 42, 0))  # 0% of the way from 24 to 42
# Output: 24.0

print(interp(102, 117, -4.0))  # -400% of the way from 102 to 117
# Output: 42.0
