import csv

#input
def userInput():
    date=input("Date: ")
    item=input("Item: ")
    category=input("Category: ")
    amount=input("Amount: ")
    float_amount = float(amount)

    return [date, item, category,float_amount]

#append to csv
def save_to_csv(data, filename = "budget.csv"):
    #save the given data to csv file
    try:
        with open(filename,"a",newline='') as csvfile:
            writer= csv.writer(csvfile)
            writer.writerow(["Date", "Item", "Category","Amount"])
            writer.writerow(data)
        print(f"Data saved to {filename}")
    except I0Error:
        print("Error: Couldn't write to the file")


if __name__=="__main__":
    user_data = userInput()
    save_to_csv(user_data)
