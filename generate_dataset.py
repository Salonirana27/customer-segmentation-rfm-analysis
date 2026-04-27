#Customer Segmentation Dataset Generator
#This code creates 1 million synthetic customer transaction records

import pandas as pd
import numpy as np
import os

#Total number of rows
n = 1000000

#create dataset folder if it does not exist
os.makedirs("dataset", exist_ok = True)

#fix random seed for same output every time
np.random.seed(42)

#Sample values for cateorical columns
regions = ["North", "South", "East", "West", "Central"]
category =["Electronics", "Fashion", "Grocery", "Home Decor", "Beauty" , "Sports"]
payment_modes = ["UPI" , "Credit card" , "Debit Card" , "Cash On Delivery", "Net Banking"]
genders = ["Male" , "Female"]

#Create main dataset
data = pd.DataFrame({
    "Transaction_ID": np.arange(1, n+1),
    "Customer_ID": np.random.randint(10001, 60001, n),
    "Age" : np.random.randint(18,66,n) ,
    "Region" : np.random.choice(regions , n) ,
    "Gender" : np.random.choice(genders,n) ,
    "Product_Category": np.random.choice(category , n),
    "Unit_Price" : np.random.randint(100 , 50001 , n),
    "Quantity" : np.random.randint(1 , 11 , n),
    "Discount_Percent" : np.random.randint(0 , 51, n) ,
    "Payment_Mode" : np.random.choice(payment_modes, n),
    "Purchase_Date" : pd.to_datetime(
        np.random.choice(pd.date_range("2023-01-01" , "2026-03-31") , n)
    )
    })
#Calculate Total bill amount before discount
data["Total_Amount"] = data["Unit_Price"] * data["Quantity"]

#Calculate Total bill amount after discount
data["Final_Amount"] = data["Total_Amount"] - (data["Total_Amount"] * data["Discount_Percent"] /100 )

#Round final amount to 2 decimal places
data["Final_Amount"] = data["Final_Amount"].round(2)

#Save dataset as CSV file
data.to_csv("dataset/customer_transactions_1M.csv" , index = False)

#display Output
print("Dataset Generated Successfully!")
print("Rows:" , data.shape[0])
print("Columns:" , data.shape[1])
print(data.head())