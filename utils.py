import csv
import pandas as pd  
import os  # study this part again

#input
def add_transaction():
    date=input("Date: ")
    item=input("Item: ")
    category=input("Category: ")
    amount=input("Amount: ")
    float_amount = float(amount)
    type_ = input("Type (income/expense): ").strip().lower()

    return [date, item, category,float_amount, type_]

#append to csv
def save_to_csv(data, filename = "data/budget.csv"):

    file_exists = os.path.isfile(filename)  # ✅ 다시 공부

    #save the given data to csv file
    try:
        with open(filename,"a",newline='') as csvfile:
            writer= csv.writer(csvfile)
            if not file_exists:
                writer.writerow(["Date", "Item", "Category","Amount","Type"])
            writer.writerow(data)
        print(f"Data saved to {filename}")
    except IOError:
        print("Error: Couldn't write to the file")



#return Data frame
def load_data(datafile):
    # with open(datafile,'r') as file:
    #     csv_reader = csv.reader(file)
    #     for row in csv_reader:
    #         print(row)
    try:
        df= pd.read_csv(datafile)
        return df
    except FileNotFoundError:
        print("No data file found")
        return pd.DataFrame(columns=["Date", "Item", "Category", "Amount", "Type"])



#summarize data 
def view_summary(datafile):
    df = load_data(datafile)
    
    #income
    income = df[df["Type"]=="income"]["Amount"].sum()
    #expenditure
    expense = df[df["Type"]=='expense']["Amount"].sum()
    #balance
    balance = income-expense

    print(f"\nIncome: {income}")
    print(f"Expenditure: {expense}")
    print(f"Balance: {balance}")

