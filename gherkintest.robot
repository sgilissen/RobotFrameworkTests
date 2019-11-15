*** Settings ***
Library  MathTestLibrary.py

*** Test Cases ***
Calc product
    When I calculate the product of ${30} and ${40}
    Then result is ${1200}

Calc square root
    When I calculate the square root of ${36}
    Then result is ${6}

*** Keywords ***
I calculate the product of ${value1} and ${value2}
    calculate product  ${value1}    ${value2}

I calculate the square root of ${value}
    calculate square root   ${value}

Result is ${result}
    result should be  ${result}