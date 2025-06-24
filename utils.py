import csv
import pandas as pd  
import os  # study this part again

#input
def add_transaction(date, item, category,amount, type_):
    # date=input("Date: ")
    # item=input("Item: ")
    # category=input("Category: ")
    # amount=input("Amount: ")
    # float_amount = float(amount)
    # type_ = input("Type (income/expense): ").strip().lower()
    #CLI to Flask

    float_amount = float(amount)

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
        df.columns = df.columns.str.strip().str.lower() 
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
        return df
    except FileNotFoundError:
        print("No data file found")
        return pd.DataFrame(columns=["Date", "Item", "Category", "Amount", "Type"])



#summarize data 
def view_summary(datafile):
    df = load_data(datafile)
    
    #income
    income = df[df["type"]=="income"]["amount"].sum()
    #expenditure
    expense = df[df["type"]=='expense']["amount"].sum()
    #balance
    balance = income-expense

    return {
        "income": income,
        "expense": expense,
        "balance": balance
    }


#extract income data
def get_total_income(datafile):
    df = load_data(datafile)
    #income
    income = df[df["type"]=="income"]["amount"].sum()
    return income

#extract expense data
def get_total_expense(datafile):
    df = load_data(datafile)
    #income
    expense = df[df["type"]=="expense"]["amount"].sum()
    return expense

#extract categorized cash flow
def get_category_cashflow(datafile):
    df=load_data(datafile)

    #make group income, expense each
    income_df = df[df["type"] == "income"].groupby("category")["amount"].sum()
    expense_df = df[df["type"] == "expense"].groupby("category")["amount"].sum()

    # Combine the income and expense series side by side into a single DataFrame
    summary_df = pd.concat([income_df, expense_df], axis=1, keys=["income", "expense"]).fillna(0)
    
    #cacluate balance
    summary_df["balance"] = summary_df["income"] - summary_df["expense"]

    # reset index to column
    return summary_df.reset_index()