*** Settings ***
Documentation   Example robot file to test the Robot Framework
Library     MathTestLibrary.py

*** Test Cases ***
calculate product
    calculate product   ${8}    ${8}
    RESULT SHOULD BE  ${64}

calculate sum
    calculate sum   ${8}    ${8}
    result should be  ${16}

calculate sum multiple
    calculate sum   ${10}    ${10}    ${10}     ${12}
    result should be    ${42}

calculate square root
    calculate square root   ${36}
    result should be    ${6}