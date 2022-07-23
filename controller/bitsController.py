import streamlit as st
from controller import itemsController

def getBitsItems():
    items = itemsController.getBitsItems()
    
    for item in items:
        if item.bits < 1:
            item['auctionPrice'] = 0
            item['afterTax'] = 0
            item['coinsPerBit'] = 999999
            continue
        auctionPrice = item.bin
        afterTax = subTractAhTax(auctionPrice)
        coinsPerBit = afterTax / item.bits
        
        item['auctionPrice'] = int(auctionPrice)
        item['afterTax'] = afterTax
        item['coinsPerBit'] = int(coinsPerBit)
    
    itemsSorted = sorted(items, key=lambda d: d.coinsPerBit, reverse=True) 
    return itemsSorted
        
            
def subTractAhTax(sellPrice):
    if sellPrice > 1000000 and sellPrice <= 1010000:
        afterTax = (sellPrice * 0.99) - (sellPrice - 1000000)
    elif sellPrice > 1010000:
        afterTax = (sellPrice * 0.98)
    else:
        afterTax = (sellPrice * 0.99)
    return int(afterTax)-350