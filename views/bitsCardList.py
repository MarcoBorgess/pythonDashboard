def formatItemPrice(price):
    formatedPrice = '0'
    if price > 1000 and price < 1000000:
        formatedPrice = '{:,.0f}'.format(price/1000) + 'k'
    elif price >= 1000000:
        formatedPrice = '{:,.2f}'.format(price/1000000) + 'm'
    elif price >= 1000000000:
        formatedPrice = '{:,.2f}'.format(price/1000000000) + 'b'
        
    return formatedPrice

def getBitsByRank(rank):
    bits = 4800
    if (rank == 'Settler'):
        bits = bits*1.1
    elif (rank == 'Citizen'):
        bits = bits*1.2
    elif (rank == 'Contributor'):
        bits = bits*1.3
    elif (rank == 'Philanthropist'):
        bits = bits*1.4
    elif (rank == 'Patron'):
        bits = bits*1.6
    elif (rank == 'Famous Player'):
        bits = bits*1.8
    elif (rank == 'Attaché'):
        bits = bits*1.9
    elif (rank == 'Ambassador'):
        bits = bits*2
    elif (rank == 'Stateperson'):
        bits = bits*2.04
    elif (rank == 'Senator'):
        bits = bits*2.08
    elif (rank == 'Dignitary'):
        bits = bits*2.12
    elif (rank == 'Councilor'):
        bits = bits*2.16
    elif (rank == 'Minister'):
        bits = bits*2.2
    elif (rank == 'Premier'):
        bits = bits*2.22
    elif (rank == 'Chancellor'):
        bits = bits*2.24
    elif (rank == 'Supreme'):
        bits = bits*2.26
    
    return int(bits)

def calculateProfit(items, bitsByRank):
    profit = 0
    coinsPerBit = 0
    buy = 0
    negative = False
    firstFiveItems = items[0:6]
    for item in firstFiveItems:
        if (item.bits < 1):
            buy = item.buyPrice
            continue
        coinsPerBit += int(item.coinsPerBit)
        
    coinsPerBit = int(coinsPerBit/5)
    sell = coinsPerBit * bitsByRank
    profit = sell - buy
    if (profit < 0):
        profit = formatItemPrice(profit*-1)
        negative = True
    else:
        profit = formatItemPrice(profit)
        
    return profit, negative

def getBitsCardList(items, rank):
    auxCard = f""" """
    style = 'positive'
    icon = '📈'
    calcatedProfit = calculateProfit(items, getBitsByRank(rank))
    profit = calcatedProfit[0]
    negative = calcatedProfit[1]
    if (negative):
        style = 'negative'
        icon = '📉'
        profit = '-' + profit

    for item in items:
        if item.idHypixel == 'BOOSTER_COOKIE':
            auxCard += f"""<div class="bits-card">
                <span class="item-name">● {item.name}</span>
                <table class="item-info">
                    <tr>
                        <td class="icon">
                            <img src="{item.iconURL}" title="{item.coinsPerBit}" height="32">
                        </td>
                        <td>
                            <span class="bits">🔷 {getBitsByRank(rank)}</span>
                        </td>
                        <td>
                            <span class="value">🔶 {formatItemPrice(item.buyPrice)}</span>
                        </td>
                        <td>
                            <span class="coins {style}">{icon} {profit}</span>
                        </td>
                    </tr>
                </table>
            </div>"""
            continue
        auxCard += f"""<div class="bits-card">
                <span class="item-name">● {item.name}</span>
                <table class="item-info">
                    <tr>
                        <td class="icon">
                            <img src="{item.iconURL}" title="{item.coinsPerBit}" height="32">
                        </td>
                        <td class="bits-cell">
                            <span class="bits">🔷 {item.bits}</span>
                        </td>
                        <td class="bits-cell">
                            <span class="value">🔶 {formatItemPrice(item.auctionPrice)}</span>
                        </td>
                        <td class="bits-cell">
                            <span class="coins">📊 {item.coinsPerBit}</span>
                        </td>
                    </tr>
                </table>
            </div>"""
        
    card = f"""
    <style>
        .container {{
            margin: 0!important;
            padding: 0!important;
        }}
        .bits-card {{
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
        .item-info {{
            margin-top: 0.5rem;
        }}
        .bits {{
            color: rgb(85, 255, 255);
        }}
        .positive {{
            color: #7cea9c!important;
        }}
        .negative {{
            color: #ff5b5b!important;
        }}
        table {{
            table-layout: fixed!important;
            width: 100%;
        }}
        tr, td {{
            border: none!important;
        }}
        .bits-cell {{
            widht: 28%;
        }}
        .icon {{
            width: 16%;
        }}
        
    </style>
    <body>
        <div class="container">
            {auxCard}
    </body>
    """
    return card