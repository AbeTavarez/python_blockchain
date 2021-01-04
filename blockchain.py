#!/usr/bin/env python3

blockchain = [[1]]


def add_value(transaction_amount):
    blockchain.append([blockchain[-1], transaction_amount])
    print(blockchain)


add_value(3)
