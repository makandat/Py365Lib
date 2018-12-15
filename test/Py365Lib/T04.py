#!/usr/bin/env python3
from Py365Lib import *
from pprint import pprint

assert Text.isdigit('0') == True
assert Text.isdigit('A') == False

assert Text.isalpha('0') == False
assert Text.isalpha('A') == True

assert Text.isdelim('0') == False
assert Text.isdelim('/') == True

assert Text.isprint('\x1b') == False  # ESC
assert Text.isprint('A') == True

print("OK")
