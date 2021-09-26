*** Settings ***
Library  main

*** Variables ***

*** Test Cases ***
test1 - Add all the elements in the array and check their sum against the expected
    array_sum   1, 2, 3, 4
    check_array_sum    10