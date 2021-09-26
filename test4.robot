*** Settings ***
Library  main

*** Variables ***

*** Test Cases ***
test4 - subtract the decimal 4 from the hexadecimal number, change the 2nd byte and compare with the correct result
    hexadecimal
    check_hexadecimal  8301dc000000e0010101c0