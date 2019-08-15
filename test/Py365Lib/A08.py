#!/usr/bin/python3
from Py365Lib import Common

# isset
print("# isset")
print(Common.isset(1))
print(Common.isset(None))

# isnull
print('# isnull')
print(Common.isnull(1))
print(Common.isnull(None))

# is_str
print('# is_str')
print(Common.is_str(0))
print(Common.is_str('ABC'))

# is_int
print('# is_int')
print(Common.is_int(0))
print(Common.is_int('ABC'))

# is_float
print('# is_float')
print(Common.is_float('0.1'))
print(Common.is_float(1))
print(Common.is_float(0.1))

# is_bool
print('# is_bool')
print(Common.is_bool(False))
print(Common.is_bool(None))
print(Common.is_bool(1))



