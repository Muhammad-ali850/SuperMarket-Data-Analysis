import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\\Users\\AAC\\Desktop\\SuperMarket Analysis.csv")

#print(df.head())
#print("Missing Values:\n", df.isnull().sum())

#print("Data Types:\n", df.dtypes)
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time'])
#print("Data Types:\n", df.dtypes)

#print("Summary:\n", df.describe())

#Date And Time
df['DateTime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'].astype(str))
df['DateTime'] = df['DateTime'].dt.tz_localize(None)
#print(df['DateTime'].head())
#print("\nData type: ", df['DateTime'].dtype)

#print("Earliest date: ", df['DateTime'].min())
#print("Latest date: ", df['DateTime'].max())

 ##df['year'] = df['datetime'].dt.year    --- we are not using this column since our data has only one year
df['month'] = df['DateTime'].dt.month
df['day'] = df['DateTime'].dt.day
df['hour'] = df['DateTime'].dt.hour
df['minute'] = df['DateTime'].dt.minute
df['weekday'] = df['DateTime'].dt.day_name()

#print(df['weekday'].value_counts())


  # ---- for further analysis uncomment below ----


'''
x = int(input("Choose analysis to run:\n"+
          "1 - Analysis of categorical columns\n"+
          "2 - Analysis of numerical columns\n"+
          "3 - Analysis of numerical columns (visualization)\n"+
          "4 - Hourly Analysis\n"+
          "5 - Weekday Analysis\n"
          "Enter number: "))
match x:
    case 1:
        #Analysis of non-numeric (categorical) columns
        cat_columns = ['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment']
        #print(df[cat_columns].dtypes)

        for x in cat_columns:
            series = df[x].value_counts()
            plt.bar(series.index, series.values)
            plt.title(x + " Analysis")
            plt.xlabel(x)
            plt.ylabel('Count')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    case 2:
        #Analysis of numerical columns
        num_columns = ['Unit price', 'Quantity', 'Tax 5%', 'Sales', 'cogs', 'gross margin percentage', 'gross income', 'Rating']
        #print(df[num_columns].dtypes)

        for x in num_columns:
            arr = df[x].values
            print('--- ' + x + ' ---',
            "\nMean       : " , round(np.mean(arr), 3),
            "\nMedian     : " , round(np.median(arr), 3),
            "\nStd Dev    : " , round(np.std(arr), 3),
            "\nMin        : " , round(np.min(arr), 3),
            "\nMax        : " , round(np.max(arr), 3))

    case 3:
        #Visualization
        num_columns = ['Unit price', 'Quantity', 'Tax 5%', 'Sales', 'cogs', 'gross margin percentage', 'gross income', 'Rating']

        for x in num_columns:
            arr2 = df[x].values
            plt.hist(arr2, bins=20, edgecolor='black')
            plt.title(x + ' Analysis')
            plt.xlabel(x)
            plt.ylabel('Frequency')
            plt.grid()
            plt.tight_layout()
            plt.show()

    case 4:
        #Hourly Analysis
        hour_counts = df['hour'].value_counts().sort_index()
        plt.figure(figsize=(14,6))
        plt.plot(hour_counts.index, hour_counts.values, marker='o')
        plt.title('Analysis by Hour')
        plt.xlabel('Hour (0-23)')
        plt.ylabel('Count')
        plt.grid()
        plt.xticks(np.arange(0,24,1))
        plt.tight_layout()
        plt.show()

    case 5:
        #Weekday Analysis
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekday_counts = df['weekday'].value_counts().reindex(week)
        plt.figure(figsize=(10,5))
        plt.bar(weekday_counts.index, weekday_counts.values)
        plt.title('Analysis by Week')
        plt.xlabel('Weekday')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
'''