import csv
import pandas as pd


def split_file(file, file_x, file_y):
    df = pd.read_csv(file)
    number = len(df.index)
    date = df["Date"].tolist()
    value = df["Value"].tolist()

    f = open(file)

    for i in range(number):
        with open(file_x, "a", newline="") as file:
            writer = csv.writer(file, delimiter="\n")
            writer.writerow([date[i]])
        f.close()


    for i in range(number):
        with open(file_y, "a", newline="") as file:
            writer = csv.writer(file, delimiter="\n")
            writer.writerow([value[i]])
        f.close()


def main():
    file = "C:/Users/evgen/Desktop/dataset.csv"
    file_x = "C:/Users/evgen/Desktop/X.csv"
    file_y = "C:/Users/evgen/Desktop/Y.csv"
    split_file(file, file_x, file_y)


if __name__ == "__main__":
    main()
