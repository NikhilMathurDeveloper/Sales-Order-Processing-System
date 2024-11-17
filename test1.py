#One query modified so that it retrieves the data of expriration from the product table.
query2 = """SELECT ProductName, Price, DateOfExpiration FROM Order1 INNER JOIN Product ON Order1.ProductID = Product.ProductID WHERE
Order1.OrderID = ?"""
#One query modified so that it retrieves the psotcode and specified address from the Client Table
query = """SELECT name, postCode, specifiedAddress FROM Order1 INNER JOIN Client On Order1.ClientID = Client.ClientiD 
WHERE Order1.OrderID = ?"""

#New body for message, which is embedded within the invoice.
body = f"""




    Subject: Pleasure doing business with you {queryCreation(OrderID)[0][0]}\n
    Product: {queryCreation2(OrderID)[0][1]}\n
    Amount: {queryCreation3(OrderID)}\n
    Date Of Expiration: {queryCreation2(OrderID)[0][2]}\n
    Post Code: {queryCreation(OrderID)[0][1]}\n,
    Specified Address: {queryCreation(OrderID)[0][2]}\n
    Date: {date.today()}\n
"""