from controller import itemsController

def getForgeItems():
    items = itemsController.getForgeItems()
    
    for item in items:
        item['auctionPrice'] = getAuctionPrice(item)
        item['afterTax'] = subTractAhTax(item.auctionPrice)
        item['ingredientsInfo'] = updateIngredients(item, items)
        item['cost'] = getItemCost(item)
        item['profit'] = item.afterTax - item.cost
        item['profitPerHour'] = int(item.profit / item.duration)
    
    itemsSorted = sorted(items, key=lambda d: d.profitPerHour, reverse=True) 
    return itemsSorted

def getItemCost(item):
    cost = 0

    for ingredient in item.ingredientsInfo:
        cost += ingredient.price * ingredient.quantity
    
    return cost

def updateIngredients(item, items):
    ingredients = eval(item.ingredients)

    ingredientsUpdated = []

    for ingredient in ingredients:
        row = {}
        row['idHypixel'] = ingredient[0]
        row['quantity'] = ingredient[1]
        row['name'] = getIngredientName(ingredient[0], items)
        row['iconURL'] = getIngredientIconURL(ingredient[0], items)
        row['price'] = getIngredientPrice(ingredient[0], items)
        row = itemsController.dotdict(row)
        ingredientsUpdated.append(row)

    return ingredientsUpdated

def getIngredientPrice(idHypixel, items):
    for item in items:
        if item.idHypixel == idHypixel:
            if item.ah:
                return item.bin
            elif item.bz:
                return item.buyPrice
    
    return None

def getIngredientIconURL(idHypixel, items):
    for item in items:
        if item.idHypixel == idHypixel:
            return item.iconURL

    return None

def getIngredientName(idHypixel, items):
    for item in items:
        if item.idHypixel == idHypixel:
            return item.name
    
    return None

def getAuctionPrice(item):
    auctionPrice = 0

    if item.ah:
        auctionPrice = item.bin
    elif item.bz:
        auctionPrice = item.sellPrice

    if item.npcSellPrice > auctionPrice:
        auctionPrice = item.npcSellPrice

    return auctionPrice

def subTractAhTax(sellPrice):
    if sellPrice > 1000000 and sellPrice <= 1010000:
        afterTax = (sellPrice * 0.99) - (sellPrice - 1000000)
    elif sellPrice > 1010000:
        afterTax = (sellPrice * 0.98)
    else:
        afterTax = (sellPrice * 0.99)
    return int(afterTax)-1200