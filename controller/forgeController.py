from controller import itemsController
import datetime

def getForgeItems():
    items = itemsController.getForgeItems()
    
    for item in items:
        item['auctionPrice'] = getAuctionPrice(item)
        item['afterTax'] = subTractAhTax(item.auctionPrice)
        item['ingredientsInfo'] = updateIngredients(item, items)
        item['cost'] = getItemCost(item)
        item['profit'] = getItemProfit(item)
        item['profitPerHour'] = getProfitPerHour(item)
    
    itemsSorted = sorted(items, key=lambda d: d.profitPerHour, reverse=True) 
    return itemsSorted

def getItemProfit(item):
    if (item.cost is None or item.afterTax is None):
        return None

    profit = item.afterTax - item.cost
    return profit

def getProfitPerHour(item):
    if (item.profit is None or item.duration is None):
        return 0

    profitPerHour = item.profit / (item.duration.total_seconds() / 3600)
    return int(profitPerHour)

def getItemCost(item):
    if (item.ingredientsInfo is None):
        return None

    cost = 0

    for ingredient in item.ingredientsInfo:
        if (ingredient.price is not None and ingredient.quantity is not None):
            cost += ingredient.price * ingredient.quantity
    
    return cost

def updateIngredients(item, items):
    if item.ingredients is None:
        return None

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
        if item.idHypixel == "COINS":
            return 1
        if item.idHypixel == idHypixel:
            if item.ah:
                return item.secondBin
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