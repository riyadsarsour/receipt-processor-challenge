import re
from datetime import datetime

def get_receipt_points(receipt):
    points = 0
    # r1 check for each alphanumeric in store name
    points += sum(c.isalnum() for c in receipt['retailer'])
    # r2: 50 pts if the total is a round dollar amount
    if float(receipt['total']).is_integer():
        points += 50
    # r3: 25 points if the total is a multiple of 0.25
    if float(receipt['total']) % 0.25 == 0:
        points += 25
    # r4: 5 points for every two items on the receipt
    points += (len(receipt['items']) // 2) * 5

    # r5: trim len of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer
    for item in receipt['items']:
        if len(item['shortDescription'].strip()) % 3 == 0:
            points += int(float(item['price']) * 0.2 + 0.99)

    #  r6: 6 points if the day of purchase is odd
    purchase_date = datetime.strptime(receipt['purchaseDate'], '%Y-%m-%d')
    if purchase_date.day % 2 != 0:
        points += 6

    #  r7: 10 points if  time of purchase is after 2pm and before 4pm
    purchase_time = datetime.strptime(receipt['purchaseTime'], '%H:%M')
    if datetime.strptime('14:00', '%H:%M') <= purchase_time < datetime.strptime('16:00', '%H:%M'):
        points += 10

    return points