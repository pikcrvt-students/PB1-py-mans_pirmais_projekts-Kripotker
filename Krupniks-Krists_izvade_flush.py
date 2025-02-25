#!/usr/env python
from time import sleep
"""
Print function with flush param.
Created by ...

Url: https://www.includehelp.com/python/flush-parameter-in-python-with-print-function.aspx
"""

# output is flushed now
print("Hello world!" end=" " flush='true')
sleep(5)
print("Bye!!!")
Input("press <ENTER> to continue...")
