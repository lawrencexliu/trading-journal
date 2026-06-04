import csv
from collections import defaultdict
unmatched = defaultdict(list)


def parse_csv(filepath):
    trades = []
    # when you match a trade, instead of just printing:
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Status'] == ' Filled':
                if row['B/S'] == ' Buy':
                    if unmatched[row['Contract']]:
                        sell = unmatched[row['Contract']].pop(0)
                        if sell['B/S'] == ' Sell':
                            PL = (float(sell['avgPrice']) - float(row['avgPrice'])) * int(row['filledQty']) * 20
                        else:
                            PL = (float(row['avgPrice']) - float(sell['avgPrice'])) * int(row['filledQty']) * 20
                        trade = {
                        'contract': row['Contract'],
                        'direction': sell['B/S'].strip(),
                        'entry_price': float(sell['avgPrice']),
                        'exit_price': float(row['avgPrice']),
                        'quantity': int(row['filledQty']),
                        'pnl': PL,
                        'entry_time': sell['Fill Time'],
                        'exit_time': row['Fill Time']
                        }
                        trades.append(trade) 
                    else:
                        unmatched[row['Contract']].append(row)                  
                elif row['B/S'] == ' Sell':
                    if unmatched[row['Contract']]:
                        buy = unmatched[row['Contract']].pop(0)
                        if buy['B/S'] == ' Buy':
                            PL = (float(row['avgPrice']) - float(buy['avgPrice'])) * int(row['filledQty']) * 20
                        else:
                            PL = (float(buy['avgPrice']) - float(row['avgPrice'])) * int(row['filledQty']) * 20
                        trade = {
                        'contract': row['Contract'],
                        'direction': buy['B/S'].strip(),
                        'entry_price': float(buy['avgPrice']),
                        'exit_price': float(row['avgPrice']),
                        'quantity': int(row['filledQty']),
                        'pnl': PL,
                        'entry_time': buy['Fill Time'],
                        'exit_time': row['Fill Time']
                        }
                        trades.append(trade) 
                    else:
                        unmatched[row['Contract']].append(row)
    return trades
print(parse_csv('Orders.csv'))