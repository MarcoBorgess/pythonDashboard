from controllers import items

def getBitsItems():
    bitsItems = items.getBitsItems()
    
    for item in bitsItems:
        if item.idHypixel == 'BOOSTER_COOKIE':
            item['auctionPrice'] = 0
            item['afterTax'] = 0
            item['coinsPerBit'] = 69420
            continue
        auctionPrice = item.bin if item.bin is not None else item.buyPrice
        afterTax = subTractAhTax(auctionPrice)
        coinsPerBit = afterTax / item.bits
        
        item['auctionPrice'] = int(auctionPrice)
        item['afterTax'] = afterTax
        item['coinsPerBit'] = int(coinsPerBit)
    
    itemsSorted = sorted(bitsItems, key=lambda d: d.coinsPerBit, reverse=True) 
    return itemsSorted
        
def subTractAhTax(sellPrice):
    if sellPrice is None:
        return 0

    if sellPrice > 1000000 and sellPrice <= 1010000:
        afterTax = (sellPrice * 0.99) - (sellPrice - 1000000)
    elif sellPrice > 1010000:
        afterTax = (sellPrice * 0.98)
    else:
        afterTax = (sellPrice * 0.99)
    return int(afterTax)-1200