import pandas
daily_sales_0 = pandas.read_csv('./data/daily_sales_data_0.csv');
daily_sales_1 = pandas.read_csv('./data/daily_sales_data_1.csv');
daily_sales_2 = pandas.read_csv('./data/daily_sales_data_2.csv');

rows = []

for row in daily_sales_0.itertuples(index=False):
    if(row.product=='pink morsel'):
        rows.append(row)
for row in daily_sales_1.itertuples(index=False):
    if(row.product=='pink morsel'):
        rows.append(row)
for row in daily_sales_2.itertuples(index=False):
    if(row.product=='pink morsel'):
        rows.append(row)

daily_sales_pm = pandas.DataFrame.from_records(rows,columns=daily_sales_0.columns)
daily_sales_pm['price'] = daily_sales_pm['price'].replace('[\$,]', '', regex=True).astype(float)
daily_sales_pm['Sales'] = daily_sales_pm['price']*daily_sales_pm['quantity']
daily_sales_pm = daily_sales_pm.drop("price",axis='columns')
daily_sales_pm = daily_sales_pm.drop("quantity",axis='columns')
daily_sales_pm.to_csv('./data/daily_sales_data_pm.csv')