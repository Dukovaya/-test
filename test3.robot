*** Settings ***
Library  main

*** Variables ***

*** Test Cases ***
test3 - сheck operation on numbers
    math_operations  4   2   +
    check_math_operations   6

    math_operations  4   2   -
    check_math_operations   2

    math_operations  4   2   *
    check_math_operations   8

    math_operations  4   2   /
    check_math_operations   2





