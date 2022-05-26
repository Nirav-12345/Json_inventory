import json
import pandas as pd
from IPython.display import display
products={1: {"name": "avocado", "price": 230,
                             "category": "grocery",
                             "quantity": 10, "date": "10/03/2021"},
                 2:      {"name": "lotion", "price": 250,
                             "category": "beauty & personal",
                             "quantity": 100,
                             "date": "15/07/2021"},
                   3:   {"name": "pain reliever", "price": 500,
                             "category": "health",
                             "quantity": 200, "date": "12/04/2021"},
                     4: {"name": "dry pasta", "price": 20,
                             "category": "grocery",
                             "quantity": 50, "date": "27/06/2021"},
                      5: {"name": "toothbrush", "price": 700,
                             "category": "beauty & personal",
                             "quantity": 100,
                             "date": "30/01/2021"},
                       6: {"name": "halloween candy", "price": 33,
                             "category": "grocery",
                             "quantity": 56, "date": "22/02/2021"},
                       7:{"name": "mascara", "price": 765,
                             "category": "beauty & personal",
                             "quantity": 70,
                             "date": "11/03/2021"},
                       8:{"name": "capsicum", "price": 764,
                             "category": "grocery",
                             "quantity": 90, "date": "16/02/2021"},
                       9:{"name": "blush", "price": 87,
                             "category": "beauty & personal",
                             "quantity": 50, "date": "17/07/2021"},
                       10:{"name": "granola bars", "price": 24,
                             "category": "grocery", "quantity": 60,
                             "date": "20/05/2021"},
                      }


js=json.dumps(products)
with open('G:\data.json','w') as f:
    f.write(js)
    f.close()
def inv():
    while 1:
        print("1)Display DataBase/All Products with there details")
        print("2","Display specific data")
        print("3","Insert data")
        print("4","Delete data")

        n=int(input())
        if n==1:
            display_data()

        elif n == 2:
            display_specific_data()

        elif n == 3:
            insert_data()

        elif n == 4:
            delete_data()

            break

        else:
            print("invalid choice")


def display_data():
        o=open('data.json','r')
        p=o.read()
        q=json.loads(p)
        n=int(input())
        if(n==1):
                    #display all records
                    table=pd.DataFrame(
                        columns=['name','weight','price'])
                    for i in q.keys():

                        temp=pd.DataFrame(columns=['name'])
                        temp['name']=i
                        for j in q[i].keys():
                            temp[j]=[q[i][j]]
                            table=table.append(temp)
                        table=table.reset_index(drop=True)
                        display(table)


def display_specific_data():
    o = open('data.json', 'r')
    p = o.read()
    q = json.loads(p)
    n = int(input())
    if n==2:
        print("enter product details you want to fetch")
        i=int(input())
        for i in q.keys():

            temp=pd.DataFrame(columns=['name'])
            temp['name']=i
            for j in q[i].keys():
                temp[j]=[q[i][j]]
            display(temp)

def insert_data():
    o = open('data.json', 'r')
    p = o.read()
    q = json.loads(p)
    n = int(input())
    if n==3:
        print("input id")
        id=int(input())
        if id not in q.keys():
            print("Product name")
            name=input()
            print("Enter price")
            price=int(input())
            q[id]={'name':name,'price':price}
        print("Enter attributes")
        z=int(input())
        if z==0:
            print("Enter name")
            nam=input()
            print("Enter product name")
            pro=input()
            q[id][nam]=pro
            print("Data added successfully")

        else:
            print("Data already [resent")

    js = json.dumps(q)
    fd = open('data.json', 'w')
    fd.write(js)
    print("Data has been written")

def delete_data():
    o = open('data.json', 'r')
    p = o.read()
    q = json.loads(p)
    n = int(input())
    if n == 4:

        print("Enter product details which you wat to delete")
        temp=input()
        if temp in q.keys():
            q.pop(temp)
            print("Product with""deleted successfully")
        else:
            print("invalid product name")

    js = json.dumps(q)
    fd = open('data.json', 'w')
    fd.write(js)
    print("Data has been deleted")



s=inv()
print(s)
