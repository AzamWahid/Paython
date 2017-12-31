Favorite_numbers = {

    'Azam':[6,8,1],
    'kashif':[3,7,4],
    'AQ': [2,0],
    'AWasey':[1,6,2],
    'jabber': [1]
}
for k,v in Favorite_numbers.items():
    print(k + "'s Favorite is")
    for value in v:
        print('\t'+ str(value))