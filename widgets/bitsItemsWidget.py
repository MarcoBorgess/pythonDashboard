def formatItemPrice(price):
    formatedPrice = ''
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

def getBitsWidget(items, rank):
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
            auxCard += f""" <div class="col-4 pl-0">
                            <div class="card-49 card-margin">
                                <div class="card-body">
                                    <div class="widget-49">
                                        <span class="widget-49-pro-title">● {item.name}</span>
                                        <div class="widget-49-title-wrapper">
                                            <img src="{item.iconURL}" title="" style="height: 32px;">
                                            <div>
                                                <div class="widget-49-meeting-info">
                                                    <span class="widget-49-bits">🔷 {getBitsByRank(rank)}</span>                                               
                                                </div>
                                                <div class="widget-49-meeting-info">
                                                    <span class="widget-49-meeting-time">🔶 {formatItemPrice(item.buyPrice)}</span>
                                                </div>
                                            </div>
                                            <div class="widget-49-meeting-info">
                                                <span class="widget-49-meeting-time {style}">{icon} {profit}</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
            """
            continue
        auxCard += f""" <div class="col-12 pl-0">
                            <div class="card-49 card-margin">
                                <div class="card-body">
                                    <div class="widget-49">
                                        <span class="widget-49-pro-title">● {item.name}</span>
                                        <div class="widget-49-title-wrapper">
                                            <img src="{item.iconURL}" title="{item.coinsPerBit}" style="height: 32px;">
                                            <div class="widget-49-meeting-info">
                                                <span class="widget-49-bits">🔷 {item.bits}</span>                                               
                                            </div>
                                            <div class="widget-49-meeting-info">
                                                <span class="widget-49-meeting-time">🔶 {formatItemPrice(item.auctionPrice)}</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
        """
        
    card = f"""
    <head>
        <meta charset="UTF-8">
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    </head>
    <style>
        .container {{
            margin: 0!important;
            padding: 0!important;
            
        }}

        .card-49 {{
            position: relative;
            display: flex;
            flex-direction: row;
            min-width: 0;
            word-wrap: break-word;
            background-color: #262730;
            background-clip: border-box;
            border: 1px solid #0e1117;
            border-radius: 8px;
            margin: 0 0 20px;
        }}

        .widget-49 .widget-49-title-wrapper {{
            display: flex;
            align-items: center;
            padding-top: 1vh;
        }}

        .widget-49 .widget-49-title-wrapper .widget-49-date-success {{
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            background-color: #7cea9c;
            border-radius: 50%;
        }}

        .widget-49 .widget-49-title-wrapper .widget-49-date-success .widget-49-date-day {{
            color: #1c7c54;
            font-weight: 900;
            font-size: 1.5rem;
            line-height: 1;
        }}

        .widget-49 .widget-49-title-wrapper .widget-49-date-success .widget-49-date-month {{
            color: #1c7c54;
            line-height: 1;
            font-size: 1rem;
            font-weight: 500;
            text-transform: uppercase;
        }}

        .widget-49 .widget-49-title-wrapper .widget-49-meeting-info {{
            display: flex;
            flex-direction: column;
            margin-left: 1rem;
        }}

        .widget-49 .widget-49-pro-title {{
            color: #fafafa;
            font-size: 1rem;
            font-weight: 700;
            overflow: hidden;
        }}

        .widget-49 .widget-49-title-wrapper .widget-49-meeting-info .widget-49-bits {{
            color: rgb(85, 255, 255);
            font-size: 1rem;
        }}
        
        .widget-49 .widget-49-title-wrapper .widget-49-meeting-info .widget-49-meeting-time {{
            color: #fafafa;
            font-size: 1rem;
        }}
        .stSelectbox {{
            width: 19%!important;
        }}
        .positive {{
            color: #7cea9c!important;
        }}
        .negative {{
            color: #ff5b5b!important;
        }}
    </style>
    <body>
        <div class="container">
            <div class="">
                {auxCard}
    </body>
    """
    return card