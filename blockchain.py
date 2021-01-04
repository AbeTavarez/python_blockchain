#!/usr/bin/env python3

blockchain = []


def get_last_bc_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([transaction_amount, last_transaction])


add_value(3)
add_value(8, get_last_bc_value())
add_value(11, get_last_bc_value())

print(blockchain)
