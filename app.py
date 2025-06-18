from utils import add_transaction, save_to_csv,view_summary

while True:
    data = add_transaction()
    save_to_csv(data)
    print("anything else?")
    input_ = input("y/n: ")
    if input_.lower()== "n":
        break

view_summary("data/budget.csv")