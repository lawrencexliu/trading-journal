import psycopg2
print("starting")
def get_connection():
    conn = psycopg2.connect(
        dbname="trading_journal",
        user="postgres",
        password="7887",
        host="localhost"
    )
    return conn

def insert_trade(conn, trade):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO trades (instrument, direction, entry_price, exit_price, quantity, pnl, entry_time, exit_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        trade['contract'],
        trade['direction'],
        trade['entry_price'],
        trade['exit_price'],
        trade['quantity'],
        trade['pnl'],
        trade['entry_time'],
        trade['exit_time']
    ))
    conn.commit()
    cursor.close()

    
from csv_parser import parse_csv

conn = get_connection()
trades = parse_csv('Orders.csv')
for trade in trades:
    insert_trade(conn, trade)
conn.close()
print("Done - inserted", len(trades), "trades")