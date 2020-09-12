# E-commerce web app Backend 
This project is a backend for T-Shirt E-Commerce which provides various endpoints/APIs to create users, login, payment processing, orders etc.

## Frameworks/3rd party tools 
* DRF (Django Rest Framework) 
* Braintree for payment gateway 

## Database
Default SQLite. 

## Backend functionality 
- category -> Django app to distinguish product categories Summer/Winter etc.
- order -> Django app to handle orders 
- payment -> Django app to integrate with Braintree Payment Gateway
- product -> Django app to maintain products provides functionality such as adding new products, maintaining invetory etc.
- user -> Django app to create users in system and also provides endpoints to login/logout. This app is based on custom User model which is implemented on top of default Django authentication module.

[Backend Structure](https://github.com/RP1807/ecom_backend/blob/master/backend_structure.pdf)

## Frontend 
There is another frontend project which consumes these APIs is implemented in ReactJS. Refer [ecom_frontend](https://github.com/RP1807/ecom_frontend)
