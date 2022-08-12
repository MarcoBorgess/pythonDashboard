import mysql.connector
import streamlit as st

class dotdict(dict):
        __getattr__ = dict.get
        __setattr__ = dict.__setitem__
        __delattr__ = dict.__delitem__

def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

def run_query(query):
    conn = init_connection()
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def run_update_query(query):
    conn = init_connection()
    with conn.cursor() as cur:
        cur.execute(query)
        conn.commit()
        return cur.rowcount

def getBitsItems():
    data = run_query(
        """
            SELECT item.idHypixel, name, rarity, category, iconURL, npcSellPrice, bits, bz, ah, item.updatedOn as itemUpdatedOn,
                bin, secondBin, ah.updatedOn as ahUpdatedOn,
                sellPrice, buyPrice, sellVolume, buyVolume, sellMovingWeek, buyMovingWeek, sellOrders, buyOrders, bz.updatedon as bzUpdatedOn
            FROM item
            LEFT JOIN ah ON ah.idHypixel = item.idHypixel
            LEFT JOIN bz ON bz.idHypixel = item.idHypixel
            WHERE bits > 0 OR item.idHypixel = 'BOOSTER_COOKIE'
        """
    )
    
    dicts = []
        
    for d in data:
        row = {}
        row['idHypixel'] = d[0]
        row['name'] = d[1]
        row['rarity'] = d[2]
        row['category'] = d[3]
        row['iconURL'] = d[4]
        row['npcSellPrice'] = d[5]
        row['bits'] = d[6]
        row['bz'] = d[7]
        row['ah'] = d[8]
        row['itemUpdatedOn'] = d[9]
        row['bin'] = d[10]
        row['secondBin'] = d[11]
        row['ahUpdatedOn'] = d[12]
        row['sellPrice'] = d[13]
        row['buyPrice'] = d[14]
        row['sellVolume'] = d[15]
        row['buyVolume'] = d[16]
        row['sellMovingWeek'] = d[17]
        row['buyMovingWeek'] = d[18]
        row['sellOrders'] = d[19]
        row['buyOrders'] = d[20]
        row['bzUpdatedOn'] = d[21]
        row = dotdict(row)
        dicts.append(row)
        
    return dicts

def getForgeItemsAndIngredientsIds():
    data = run_query(
        """
            SELECT idHypixel, ingredients FROM forge WHERE active = 1
        """
    )

    itemsIdHypixel = []

    for item in data:
        idHypixel = item[0]
        ingredients = eval(item[1])

        itemsIdHypixel.append(idHypixel)
        
        for ingredient in ingredients:
            ingredientIdHypixel = ingredient[0]
            if ingredientIdHypixel not in itemsIdHypixel:
                itemsIdHypixel.append(ingredientIdHypixel)

    return itemsIdHypixel

def getForgeItems():
    idsHypixel = getForgeItemsAndIngredientsIds()
    idsHypixel = tuple(idsHypixel)

    data = run_query(
        """
            SELECT item.idHypixel, name, rarity, category, iconURL, npcSellPrice, bits, bz, ah, item.updatedOn as itemUpdatedOn,
                bin, secondBin, ah.updatedOn as ahUpdatedOn,
                sellPrice, buyPrice, sellVolume, buyVolume, sellMovingWeek, buyMovingWeek, sellOrders, buyOrders, bz.updatedon as bzUpdatedOn,
                hotm, duration, ingredients
            FROM item
            LEFT JOIN ah ON ah.idHypixel = item.idHypixel
            LEFT JOIN bz ON bz.idHypixel = item.idHypixel
            LEFT JOIN forge ON forge.idHypixel = item.idHypixel
            WHERE item.idHypixel IN {}
        """.format(idsHypixel)
    )

    items = []

    for item in data:
        row = {}
        row['idHypixel'] = item[0]
        row['name'] = item[1]
        row['rarity'] = item[2]
        row['category'] = item[3]
        row['iconURL'] = item[4]
        row['npcSellPrice'] = item[5]
        row['bits'] = item[6]
        row['bz'] = item[7]
        row['ah'] = item[8]
        row['itemUpdatedOn'] = item[9]
        row['bin'] = item[10]
        row['secondBin'] = item[11]
        row['ahUpdatedOn'] = item[12]
        row['sellPrice'] = item[13]
        row['buyPrice'] = item[14]
        row['sellVolume'] = item[15]
        row['buyVolume'] = item[16]
        row['sellMovingWeek'] = item[17]
        row['buyMovingWeek'] = item[18]
        row['sellOrders'] = item[19]
        row['buyOrders'] = item[20]
        row['bzUpdatedOn'] = item[21]
        row['hotm'] = item[22]
        row['duration'] = item[23]
        row['ingredients'] = item[24]
        row = dotdict(row)
        items.append(row)
        
    return items

def getForgeItemsIds():
    data = run_query(
        """
            SELECT name, iconURL, active, forge.idHypixel
            FROM forge
            INNER JOIN item ON item.idHypixel = forge.idHypixel
        """
    )
    
    items = []
    
    for item in data:
        row = {}
        row['name'] = item[0]
        row['iconURL'] = item[1]
        row['active'] = item[2]
        row['idHypixel'] = item[3]
        row = dotdict(row)
        items.append(row)
    
    itemsSorted = sorted(items, key=lambda d: d.active, reverse=True)
    return itemsSorted

def updateForgeItemActive(idHypixel, active):
    query = """
        UPDATE forge
        SET active = {}
        WHERE idHypixel = '{}'
    """.format(active, idHypixel)
    
    rows = run_update_query(query)
    if rows > 0:
        return True