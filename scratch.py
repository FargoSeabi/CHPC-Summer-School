reviews.query("App in @apps.App", inplace=True)

# 1
valid_apps = apps["Apps"]

reviews.query("App in @valid_apps", inplace=True)

# 2

reviews = reviews.loc[reviews["App"].isin(valid_apps)]

# 3 

reviews = reviews[reviews["App"].isin(valid_apps)]


apps = apps.join(aggregated_reviews, on="App", how="left")

apps = apps.merge(aggregated_reviews, on="App", how="left")
