from db import get_connection
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT pnl FROM trades")
results = cursor.fetchall()

pnl_list = []
for row in results:
    pnl_list.append(row[0])


positive = 0
negative = 0 
neutral = 0
for trade in pnl_list:
    if trade > 0:
        positive += 1
    elif trade < 0:
        negative += 1
    else:
        neutral += 1

winrate = 0.0 
if len(pnl_list) > 0:
    winrate = positive / len(pnl_list) * 100
else:
    winrate = 0

print(winrate)