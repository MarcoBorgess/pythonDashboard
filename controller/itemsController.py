from collections import namedtuple
import streamlit as st
import mysql.connector

def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

def run_query(query):
    conn = init_connection()
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def getBitsItems():
    data = run_query(
        """
            SELECT item.idHypixel, name, rarity, category, iconURL, npcSellPrice, bits, bz, ah, item.updatedOn as itemUpdatedOn,
                bin, secondBin, ah.updatedOn as ahUpdatedOn,
                sellPrice, buyPrice, sellVolume, buyVolume, sellMovingWeek, buyMovingWeek, sellOrders, buyOrders, bz.updatedon as bzUpdatedOn
            FROM item
            LEFT JOIN ah ON ah.idHypixel = item.idHypixel
            LEFT JOIN bz ON bz.idHypixel = item.idHypixel
            WHERE bits > 0
            UNION
            SELECT item.idHypixel, name, rarity, category, iconURL, npcSellPrice, bits, bz, ah, item.updatedOn as itemUpdatedOn,
                bin, secondBin, ah.updatedOn as ahUpdatedOn,
                sellPrice, buyPrice, sellVolume, buyVolume, sellMovingWeek, buyMovingWeek, sellOrders, buyOrders, bz.updatedon as bzUpdatedOn
            FROM item
            LEFT JOIN ah ON ah.idHypixel = item.idHypixel
            LEFT JOIN bz ON bz.idHypixel = item.idHypixel
            WHERE item.idHypixel = 'BOOSTER_COOKIE'
        """
    )
    
    dicts = []
    
    class dotdict(dict):
        __getattr__ = dict.get
        __setattr__ = dict.__setitem__
        __delattr__ = dict.__delitem__
        
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