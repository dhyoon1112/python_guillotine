

payers = {}

def list_items(subtotal, tax, tip):

    items = []
    item = 0

    while item != "done":
        items.append(float(item))
        item = input("Enter item cost for this payer (Enter 'done' when there are no more items): ")
        print(items)
        
    payer = str(input("Who paid for these items? "))
    payer_subtotal = sum(items)
    payer_tax = round((payer_subtotal / subtotal) * tax,2)
    payer_tip = round((payer_subtotal / subtotal) * tip,2)

    details = [payer, payer_subtotal, payer_tax, payer_tip]

    payer_dict = {'Payer': details[0], 'Subtotal': details[1], 'Tax': details[2], 'Tip': details[3]}
    print(payer_dict)

    return payer_dict


total = float(input("Enter total: "))
subtotal = float(input("Enter subtotal: "))
tax = float(input("Enter tax amount: "))
tip = float(input("Enter tip amount: "))


'''
subtotal = 100
tax = 10
tip = 10
'''

list_items(subtotal, tax, tip)



