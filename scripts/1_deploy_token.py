from brownie import JKJToken
from scripts.helpful_script import get_account
from web3 import Web3

initial_support = Web3.toWei(1000, "ether")


def main():
    account = get_account()
    jkj_token = JKJToken.deploy(initial_support, {"from": account})
    print(jkj_token.name())
