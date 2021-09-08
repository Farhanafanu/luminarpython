products=[
    {"p_name":"complan","mrp":230,"avl_qty":50},
    {"p_name": "horlicks", "mrp": 250, "avl_qty": 10},
    {"p_name": "bournvita", "mrp": 220, "avl_qty": 0},
    {"p_name": "nutricharge", "mrp": 200, "avl_qty": 100},
    {"p_name": "mylo", "mrp": 100, "avl_qty": 0},

]
product_name=list(map(lambda item:item["p_name"],products ))
print(product_name)
avail_product=list(filter(lambda item:item["avl_qty"]>0,products))
print(avail_product)
product_name=list(map(lambda item:item["p_name"],products))
print(product_name)
available_product=list(filter(lambda item:item["avl_qty"]>0,products))
print(available_product)
out_stock=list(filter(lambda item:item["avl_qty"]==0,products))
print(out_stock)
prices=list(map(lambda item:item["mrp"],products))
print(max(prices))
print(min(prices))
print(prices)
out_stock=list(filter(lambda item:item["avl_qty"]==0,products))
print(out_stock)
prices=list(map(lambda prod:prod["mrp"],products))
print(max(prices))
print(min(prices))
