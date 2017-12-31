Cities={
    'Karachi' : {
        'Country':'Pakistan',
        'Population': 21100000,
        'Fact' : 'Karachi generates 35% of Pakistan’s Tax revenue'

    },
    'New York': {
        'Country': 'United States of America',
        'Population': 8538000,
        'Fact': "In 2018 NYC will open the world's first underground park"

    },
    'Paris':{
        'Country': 'France',
        'Population': 2241346,
        'Fact': "A high maintenance monument"
   }
}
for key,value in Cities.items():
    print('\nCity: ' + key)
    Country = value['Country']
    Population = value['Population']
    Fact = value['Fact']

    print('\tCountry: ' + Country)
    print('\tPopulation: ' + str(Population))
    print('\tFact: ' + Fact)