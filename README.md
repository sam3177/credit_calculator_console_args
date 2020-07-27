# credit_calculator_console_args

Using command-line arguments you can run your program this way:
python credit_calc.py --type=diff --principal=1000000 --periods=10 --interest=10
In that case, your program can get different values and not ask the user to input them. 

"--type" indicates the type of payments: "annuity" or "diff" (differentiated).

"--principal" is used for calculations of both types of payment. You can get its value knowing the interest, annuity payment and periods.

"--periods" parameter denotes the number of months and/or years needed to repay the credit. It's calculated based on the interest, annuity payment and principal.

"--interest" is specified without a percent sign. Note that it may accept a floating-point value. Our credit calculator can't calculate the interest, so it must be specified as arg, otherwise the program throws the general error message: "Incorrect parameters"

