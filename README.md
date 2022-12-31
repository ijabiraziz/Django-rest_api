# Django REST Framework API

This repository contains a Django project that demonstrates how to create a REST API for managing stock data. The API includes the following features:

- A main API that fetches data for a given stock symbol, including 10 rows of insider transaction data and related valuation data
- An insider transaction API that fetches all insider transaction data for a given stock symbol, with optional filters for cost
- A valuation API that fetches valuation data for a given stock symbol and calculates the market cap per share
- A POST API for saving data in the stock and insider transactions tables

## Prerequisites

- Python 3.7 or higher
- Django 3.1 or higher
- Django REST framework 3.11 or higher

## Installation

1. Clone the repository:
 
    git clone https://github.com/jabiraziz/Django-rest_api.git
    
2. Navigate to the project directory:
    cd assessment
    
    
   Open terminal
3. Install the required packages:
   pip install -r requirements.txt
   
   Then 
   python manage.py makemigrations
   python manage.py migrate

   Now that everything is settle, go on and run the server using below command
   python manage.py runserver
   
   Now open broweser and navigate to http://127.0.0.1:8000/
 
 
 
#### API's
#### Main API

To fetch data for the stock symbol "AAPL", including 10 rows of insider transaction data and related valuation data,
send a GET request to the following URL: http://localhost:8000/AAPL/ (instead of AAPLE you can also pass GOOG,MSFT or FB)


#### Insider Transaction API

To fetch all insider transaction data for the stock symbol "AAPL", send a GET request to the following URL: http://localhost:8000/insider-transactions/AAPL/
and To filter the data by 'cost', pass a cost parameter in the URL:http://localhost:8000/insider-transactions/AAPL/?cost=1000 , This will return all rows with a cost equal to or greater than 1000. If the cost parameter is not included in the URL, all data will be returned.
So in a sense 'cost' parameter is optional


#### Valuation API

To fetch valuation data for the stock symbol "AAPL" and calculate the market cap per share,
send a GET request to the following URL: http://localhost:8000/valuation/AAPL/


#### Post API
To save data in the stock and insider transactions tables, follow the url:http://localhost:8000/post-data/
and the data should be in such format :
{
  "symbol": "AAPL",
  "name": "Apple Inc.",
  "price": 100,
  "change": 0.5,
  "insider_transactions": [
    {
      "name": "ABC",
      "cost": 1000
    },
    {
      "name": "XYZ",
      "cost": 2000
    }
  ]
}

if the symbol already exists, api will through an error else your data will be saved.

Note: inside assessment directory i have also included the collection of api endpoints you can definitly check it on Postman.

Thanks,

Jabir Aziz
