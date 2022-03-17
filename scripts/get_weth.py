from scripts.helpful_scripts import get_account_v2
from brownie import interface, config, network
from web3 import Web3

def main():
    get_weth()

def get_weth():
    """
    Mints weth by depositing eth
    """
    account = get_account_v2()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])

    tx = weth.deposit({"from": account, "value": 0.1 * 10**18})
    tx.wait(1)
    print("Received 0.1 weth")
    return tx