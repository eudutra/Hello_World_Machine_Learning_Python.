from pandas import read_csv

# Load dataset
file = 'vgsales.csv'
names = ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
dataset = read_csv(file, names=names)

# print(dataset.shape)
# print(dataset.describe)
# print(dataset.head())
# print(dataset.head(10))
# print(dataset.tail())
# print(dataset.tail(10))
# qtde_wii = dataset[(dataset['Platform'] == 'Wii')]
# print(len(qtde_wii))
# qtde_x360 = dataset[(dataset['Platform'] == 'X360')]
# print(len(qtde_x360))
# qtde_ps4 = dataset[(dataset['Platform'] == 'PS4')]
# print(len(qtde_ps4))

# qtde_wii.to_csv('wii.csv')
