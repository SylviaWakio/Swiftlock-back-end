
5. Access the app in your web browser at `http://localhost:5000.

## Usage

1. Create an account or log in to an existing one.

2. Start adding products to your inventory.

3. Organize products into categories for better management.

4. Use the search and filter features to find specific items quickly.

5. Generate reports to track inventory changes and trends.

## Feature
This is an inventory management system written in falsk 
 The local installation of flask `http://localhost:5000`.
  Also the local installation of flask  is provided as "flask-masterr" which can be run as "python setup.py install". 
  The project is run through "flask run".
  I have provided way to extract the transaction info in a csv format as "data-extract.py".
   The main page lists all the items. 
   Clicking the name of any of the itmes will take you to the transaction page (Transfer/Return) page. 
   Here clicking on Transfer/Return will take you to confirmation page providing you with the transaction number. 
   The date of transcation is auto-added by the system as the present date.
   Also by going to the flask admin page ("homepage/admin") will let you Create, Read, Update and Delete Items, Clients (supposed to receive or return items), Categories and Transactions.
    Dont forward, back or reload pages as that may lead to redundant data. Also,search can be based on any of the components - Name, Category,No. of items, Item No. and it will work seamlessly.Transact by using buttons on the page only.

