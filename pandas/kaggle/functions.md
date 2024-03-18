import pandas as pd

- Create dataframe
```pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])```

- create series
```pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')```

- Read csv
```reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")```

- get #rows and #columns
```reviews.shape```

- get first 5 rows
```reviews.head()```

- select a column
```reviews.country``` or ```reviews["country"]```

- select a row of a specific index
```reviews.iloc[0]```

- select a column of a specific index
```reviews.iloc[:, 0]```

- other types of selection by index:
    - ```reviews.iloc[:3, 0]```
    - ```reviews.iloc[[0, 1, 2], 0]```
    - ```reviews.iloc[-5:]```

- selection based on label
```reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]```


- How often does each country appear in the dataset?
```reviews_per_country = reviews.country.value_counts()``` or ```reviews.groupby('country').country.count()```

- title of the wine with the highest points-to-price ratio
```bargain_wine = reviews.loc[(reviews.points / reviews.price).idxmax(), 'title']```

- get the cheapest wine in each point value category
```reviews.groupby('points').price.min()```

- get the best wine by country and province
```reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])```

- functional language (high order functions):
```
def rate(row):
    if row["country"]=="Canada" or row.points>=95:
        return 3
    elif row.points>=85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(rate, axis='columns')
```