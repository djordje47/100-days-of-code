def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]
coinsDict = {'galleons': 100, 'sickles': 50, 'knuts': 25}


# print(total(*coins), 'Knuts')
# print(total(sickles=50, galleons=100, knuts=25), 'Knuts')
# print(total(**coinsDict), 'Knuts')

def f(*args, **kwargs):
    print("Named:", kwargs)
    print("Positional:", args)

f(galleons=100, sickles=50, knuts=25)