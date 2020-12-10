'''
A new shop consists of a maximum of five different items like shoes, socks, belts, shiners, and bags. 
The items are in priority order that means shoes are of the highest priority and bags have the lowest priority.  
It maintains an inventory list manually which consists of the price of each item and the quantity (stock) of that
item present in that shop. For example three items (shoes, socks, and belts) with 5 shoes each of 1000/-, 3 socks
each of 100/- and 4 belts each of 300/-. This shoe company owner hires you to make an automated system such that 
your code could calculate the total stock and total cost of the inventory. It should also calculate the total cost 
of each item in the inventory. Design a python code using dictionaries to do this job with functions .

 

Input Format:

In the first line, get the number of items.

For every items, get the following details in a new line

Item name 1

Cost of the item 1

Number of stocks of that item 1

.

.

.

Item name ‘n’

Cost of the item ‘n’

Number of stocks of that item ‘n’

 

The input depends on the number of items entered by the user. Priority also matters. If the number of items is 3, 
then the first entry is shoes then socks and then belt. If the number of items is 4 then the first entry is shoes, 
then socks followed by the belt and finally shiner. The price and the stock entry is given in the example are just 
indicative.

 

Output Format:

For every item print the following in new lines.

Name of the item 1

Total cost of the item 1

.

.

.

Name of the item ‘n’

Total cost of the item ‘n’

Total stock of all the items

Total inventory cost of all the items correct to two decimal places

 

Sample Input 1:

2

shoes

1000

5

socks

100

3

 

Sample Output 1:

shoes

5000.00

socks

300.00

8

5300.00

 

Sample Input 2:

3

shoes

1000

5

socks

100

3

belts

500

2

 

Sample Output 2:

shoes

5000.00

socks

300.00

belts

1000.00

10

6300.00

_______________________

Input
2
shoes
1000
5
socks
100
3
Expected output
shoes
5000.00
socks
300.00
8
5300.00
Your Program Output
shoes
5000.00
socks
300.00
8
1100.00
'''
#Code Author : Pranav Viswanathan
number = int(input())
def Func_Dictionaries(n):
    totPrice = 0
    cnt = 0
    d = {}
    tot = 0
    for i in range (0,n):
        nameOfItem = (input())
        costOfTheItem = float(input())        
        number = int(input())
        tot = tot + number
        totPrice = (totPrice + (costOfTheItem * number))
        d[i] = {
            'name' : nameOfItem,
            'cost' : costOfTheItem * number
            }

    for i in range (0,n):
        
        print(d[i]['name'])
        print('{:.2f}'.format(float(d[i]['cost'])))
    print(tot)
    print('{:.2f}'.format(totPrice))

Func_Dictionaries(number)
