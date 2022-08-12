def formatItemPrice(price):
    formatedPrice = str(price)

    isNegative = False
    if price < 0:
        price = abs(price)
        isNegative = True

    if price > 1000 and price < 1000000:
        formatedPrice = '{:,.0f}'.format(price/1000) + 'k'
    elif price >= 1000000:
        formatedPrice = '{:,.2f}'.format(price/1000000) + 'm'
    elif price >= 1000000000:
        formatedPrice = '{:,.2f}'.format(price/1000000000) + 'b'
    
    if isNegative and price > 1000:
        formatedPrice = '-' + formatedPrice
    
    return formatedPrice

def getIconByPrice(price):
    if price < 0:
        return '🔴'
    elif price > 0:
        return '🟢'
    else:
        return '🟤'

def getForgeCardList(items, hotm):
    auxCard = f""" """
    for item in items:
        ingCard = f""""""
        if item.hotm is not None and int(item.hotm) <= int(hotm):
            for ingredient in item.ingredientsInfo:
                ingCard += f"""<td class="td-icon">
                        <img src="{ingredient.iconURL}" alt="{ingredient.name}" height="24" class="ingredient-icon">
                    </td>
                    <td>
                        <span>{ingredient.quantity}x {ingredient.name}</span>
                    </td>
                    <td>
                        <span>🔵 {formatItemPrice(ingredient.price)}</span>
                    </td>
                    <td>
                        <span>🟣 {formatItemPrice(ingredient.total)}</span>
                </tr>"""
            auxCard += f"""<div class="forge-card">
                <span class="item-duration">{item.formatedDuration}</span>
                <table class="item-info">
                    <tr>
                        <td class="td-icon">
                            <img src="{item.iconURL}" title="{item.name}" height="32">
                        </td>
                        <td>
                            <span class="item-name"> {item.name}</span>
                        </td>
                        <td class="forge-cell">
                            <span class="price" title="Cost">🔵 {formatItemPrice(item.cost)}</span>
                        </td>
                        <td class="forge-cell">
                            <span class="price" title="Sell Price">🟣 {formatItemPrice(item.auctionPrice)}</span>
                        </td>
                    </tr>
                    {ingCard}
                    <tr>
                        <td colspan ="4">
                            <span title="Profit">{getIconByPrice(item.profit)} {formatItemPrice(item.profit)}</span>
                            <span title="Profit per Hour">⏲️ {formatItemPrice(item.profitPerHour)}</span>
                        </td>
                    </tr>
                </table>
            </div>"""
        
    card = f"""
    <style>
        .forge-card {{
            color: #fafafa;
            line-height: 1;
            background-color: #262730;
            border: 1px solid #0e1117;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 1rem;
        }}
        .item-name {{
            font-size: 1rem;
            font-weight: 700;
        }}
        .item-duration {{
            float: right; 
            color: grey;
        }}
        .td-icon {{
            width: 5%;
        }}
        .span-col {{
            display: flex;
            flex-direction: column;
            padding: 5px 0 5px 0;
        }}
        .ingredient-icon {{
            margin-left: 30%;
        }}
    </style>
    <body>
        <div class="container">
            {auxCard}
    </body>
    """
    return card