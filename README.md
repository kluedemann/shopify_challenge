## Answers
1. 
    a) It is likely there are commercial transactions and a mispriced item which are skewing the mean. See explanation below and included code.


    b) Without modifying the data set to remove outliers/errors, the median order value is the best metric.


    c) The median order value is $284.


2. a) 54
```
SELECT COUNT(*) FROM Orders O, Shippers S WHERE O.ShipperID = S.ShipperID AND S.ShipperName = 'Speedy Express';
```
2. b) Peacock; 
```
SELECT E.LastName
FROM Orders O, Employees E
WHERE E.EmployeeID = O.EmployeeID
GROUP BY E.LastName
HAVING COUNT(*) = (
    SELECT MAX(NumOrders) 
    FROM (
        SELECT COUNT(*) as NumOrders 
        FROM Orders O2 
        GROUP BY O2.EmployeeID));
```
2. c) Gorgonzola Telino;
```
SELECT P.ProductName
FROM Orders O, Products P, Customers C, OrderDetails D
WHERE O.OrderID = D.OrderID AND D.ProductID = P.ProductID AND C.CustomerID = O.CustomerID AND C.Country = 'Germany'
GROUP BY P.ProductName
HAVING COUNT(*) = (
    SELECT MAX(NumOrders) 
    FROM (
        SELECT COUNT(*) as NumOrders 
        FROM Orders O2, Customers C2, OrderDetails D2
        WHERE D2.OrderID = O2.OrderID AND O2.CustomerID = C2.CustomerID AND C2.Country = 'Germany'
        GROUP BY D2.ProductID));
```

## Explanation
I used SQL queries to examine the dataset. I primarily searched for orders over $2000.
The high average order value is due to outliers in the dataset.
Firstly, there are recurring orders of $704000 at exactly 4:00:00.
Due to the consistent volume and time, this is likely a commercial transaction such as an inventory purchase.
Secondly, it is likely that a product's price is being entered incorrectly into the system.
There are many transactions that are multiples of $25725, with the other factor being the number of items.
Considering the median order value of $284, I predict that a shoe priced at $257.25 is being purchased.
However, the decimal is missing from the item's price in the data.

The median is not sensitive to outliers, so it will still provide a reasonable aggregate measure.
I used python to calculate the median.
