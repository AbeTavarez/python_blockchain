#!/usr/bin/env python3

# * Init Blockchain list
blockchain = []


def get_last_bc_value():
    """ Returns last value on the blockchain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value to the back of the blockchain.
    Arguments:
      :transaction_amount: The amount that should be added.
      :last_transaction: The last blockchain transaction (default [1])
    """
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """ Returns the input of the user (a new transaction amount) as a float. """
    return float(input('Enter transaction amount: '))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = float(input('Enter transaction amount: '))
add_value(last_transaction=get_last_bc_value(), transaction_amount=tx_amount)

tx_amount = float(input('Enter transaction amount: '))
add_value(tx_amount, get_last_bc_value())

print(blockchain)
