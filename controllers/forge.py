from controllers import items

def getSortedForgeItems():
    forgeItems = items.getForgeItems()
    
    for forgeItem in forgeItems:
        forgeItem['auctionPrice'] = getAuctionPrice(forgeItem)
        forgeItem['afterTax'] = subTractAhTax(forgeItem.auctionPrice)
        forgeItem['ingredientsInfo'] = updateIngredients(forgeItem, forgeItems)
        forgeItem['cost'] = getItemCost(forgeItem)
        forgeItem['profit'] = getItemProfit(forgeItem)
        forgeItem['profitPerHour'] = getProfitPerHour(forgeItem)
        forgeItem['formatedDuration'] = getFormatedDuration(forgeItem)
    
    itemsSorted = sorted(forgeItems, key=lambda d: d.profitPerHour, reverse=True) 
    return itemsSorted

def getFormatedDuration(forgeItem):
    if (forgeItem.duration is None):
        return 0

    formatedDuration = ''
    tdelta = forgeItem.duration
    days = tdelta.days
    hours, rem = divmod(tdelta.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    
    if days > 0:
        formatedDuration += str(days) + "d "
    if hours > 0:
        formatedDuration += str(hours) + "h "
    if minutes > 0:
        formatedDuration += str(minutes) + "m "
    if seconds > 0:
        formatedDuration += str(seconds) + "s "

    return formatedDuration

def getItemProfit(forgeItem):
    if (forgeItem.cost is None or forgeItem.afterTax is None):
        return 0

    profit = forgeItem.afterTax - forgeItem.cost
    return profit

def getProfitPerHour(forgeItem):
    if (forgeItem.profit is None or forgeItem.duration is None):
        return 0

    profitPerHour = forgeItem.profit / (forgeItem.duration.total_seconds() / 3600)
    return int(profitPerHour)

def getItemCost(forgeItem):
    if (forgeItem.ingredientsInfo is None):
        return None

    cost = 0

    for ingredient in forgeItem.ingredientsInfo:
        if (ingredient.price is not None and ingredient.quantity is not None):
            cost += ingredient.price * ingredient.quantity
    
    return cost

def updateIngredients(forgeItem, forgeItems):
    if forgeItem.ingredients is None:
        return None

    ingredients = eval(forgeItem.ingredients)

    ingredientsUpdated = []

    for ingredient in ingredients:
        row = {}
        row['idHypixel'] = ingredient[0]
        row['quantity'] = ingredient[1]
        row['name'] = getIngredientName(ingredient[0], forgeItems)
        row['iconURL'] = getIngredientIconURL(ingredient[0], forgeItems)
        row['price'] = getIngredientPrice(ingredient[0], forgeItems)
        row['total'] = row['price'] * row['quantity']
        row = items.dotdict(row)
        ingredientsUpdated.append(row)

    return ingredientsUpdated

def getIngredientPrice(idHypixel, forgeItems):
    for forgeItem in forgeItems:
        if forgeItem.idHypixel == idHypixel:
            if forgeItem.ah:
                return forgeItem.secondBin
            elif forgeItem.bz:
                return forgeItem.buyPrice
    
    return 1

def getIngredientIconURL(idHypixel, forgeItems):
    for forgeItem in forgeItems:
        if forgeItem.idHypixel == idHypixel:
            return forgeItem.iconURL

    return None

def getIngredientName(idHypixel, forgeItems):
    for forgeItem in forgeItems:
        if forgeItem.idHypixel == idHypixel:
            return forgeItem.name
    
    return None

def getAuctionPrice(forgeItem):
    auctionPrice = 0

    if forgeItem.ah:
        auctionPrice = forgeItem.bin
    elif forgeItem.bz:
        auctionPrice = forgeItem.sellPrice

    if forgeItem.npcSellPrice > auctionPrice:
        auctionPrice = forgeItem.npcSellPrice

    return auctionPrice

def subTractAhTax(sellPrice):
    if sellPrice > 1000000 and sellPrice <= 1010000:
        afterTax = (sellPrice * 0.99) - (sellPrice - 1000000)
    elif sellPrice > 1010000:
        afterTax = (sellPrice * 0.98)
    else:
        afterTax = (sellPrice * 0.99)
    return int(afterTax)-1200