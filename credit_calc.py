import math
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--principal", type=float, help="principal")
parser.add_argument("--interest", type=float, help="interest")
parser.add_argument("--periods", type=int, help="periods")
parser.add_argument("--payment", type=float, help="payment")
parser.add_argument("--type", type=str, help="type")
args = parser.parse_args()

principal = args.principal
interest = args.interest
periods = args.periods
annuity = args.payment
type_ = args.type
if interest is not None:
    i = interest / 100 / 12  # nominal interest rate

#  check if any value is negative and we will use len()
#  of the result as condition to break the app
values = [principal, interest, periods, annuity]
neg_signs = list(filter(lambda x: x < 0, list(filter(lambda x: x is not None, values))))


def months_count():
    x = annuity / (annuity - i * principal)
    n = math.ceil(math.log(x, 1 + i))
    overpayment = round(annuity * n - principal)
    years, months = n // 12, n % 12
    #  pluralize (or not) the output
    if years == 1:
        s = ''
    else:
        s = 's'
    if months == 1:
        s_ = ''
    else:
        s_ = 's'

    if years > 0 and months > 0:
        print('You need {} year{} and {} month{} to repay this credit!'.format(years, s, months, s_))
    elif years == 0:
        print('You need {} month{} to repay this credit!'.format(months, s_))
    elif months == 0:
        print('You need {} year{} to repay this credit!'.format(years, s))
    print('Overpayment = {}'.format(overpayment))


def annuity_count():
    ann = math.ceil(principal * (i * math.pow(i + 1, periods)) / (math.pow(i + 1, periods) - 1))
    overpayment = round(ann * periods - principal)
    print('Your annuity payment = {}!'.format(ann))
    print('Overpayment = {}'.format(overpayment))


def credit_count():
    credit_ = math.floor(annuity / ((i * math.pow(i + 1, periods)) / (math.pow(i + 1, periods) - 1)))
    overpayment = round(annuity * periods - credit_)
    print('Your credit principal = {}!'.format(credit_))
    print('Overpayment = {}'.format(overpayment))


def differential():
    payment_sum = 0
    for k in range(1, periods + 1):
        diff_payment = math.ceil(principal / periods + i * (principal - principal * (k - 1) / periods))
        payment_sum += diff_payment
        print('Month {}: paid out {}'.format(k, diff_payment))
    overpayment = int(payment_sum - principal)
    print('\nOverpayment = {}'.format(overpayment))


def calculate():
    if len(sys.argv) != 5:
        print('Incorrect parameters')
    elif interest is None:
        print('Incorrect parameters')
    elif len(neg_signs) != 0:
        print('Incorrect parameters')
    else:
        if type_ is None:
            print('Incorrect parameters')
        elif type_ == 'annuity':
            if periods is None:
                return months_count()
            elif annuity is None:
                return annuity_count()
            elif principal is None:
                return credit_count()
        elif type_ == 'diff' and annuity is not None:
            print('Incorrect parameters')
        elif type_ == 'diff':
            return differential()
        else:
            print('Incorrect parameters')


calculate()
