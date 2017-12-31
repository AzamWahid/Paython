favorite_places={
    'Adil': ['Sea view','Parks','Food Shop','Home'],
    'Rizwan' : ['Karachi','Quetta','Hyderabd'],
    'Yaseen' : ['Defence','Atrium']
}
for key,values in favorite_places.items():
    print(str(key) + "'s Favorite Places is")
    for value in values:
        print('\t'+value)