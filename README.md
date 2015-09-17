#Auction-men
Auction-men is a platform where users can insert auctions about products and services, place a bid for one or more of them. When the deadline is reached, user that placed the largest bid wins the auction.
For authenticated users, in any moment it's possible to have an overview of the running auction, place a bid and watch the bid history and purchased history of products.
Users that are not logged in are able to view only recents auction as guests.

##Installation
To enjoy auction-men follow these step, in the same order they're written.
 
Auction-men is written in Python 2.7 using Django Framework 1.8.x

### Requirements
To run auction-men you must have this libraries installed on your machine.

#### Python and Django libraries

- djagno-crispy-forms
- django-registration-redux

If you have `pip` installed you can easily download these requirements running:

    pip install django-crispy-forms==1.4.0
    pip install django-registration-redux=1.2
    
#### Javascript requirements

- twitter bootstrap
- bootstrap horizon
- jQuery
- jQuery countdown

If you have `bower` installed you can easily download these requirements running:

    bower install bootstrap
    bower install jquery
    bower install bootstrap-horizon
    bower install jquery.countdown
    
### Database
In order to run auction-men requires you have MySQL database installed on your machine.
To create the db running these commands on your terminal:

    $ mysql -u [user] -p
    mysql> create database auctions_db;
    mysql> create user 'auctions_admin'@'localhost' identified by [your pwd here];
    mysql> grant all privileges on auctions_db.* to'auctions_admin'@'localhost' with grant options;
   
We provide a sample db, in order to starting enjoy the auction-men capability as soon as possible.
Any informations in this database are not related to real people, product or other kind of entity and are provided only as an example of what this project can do.

To import this data in your db after you created it, run this command:

    $ cd /path/to/auctions_men
    $ mysql -u [user] -p [password] auctions_db < auctions_db_dump.sql
    
## Starting the server
    
    $ cd /path/to/auctions_men
    $ python manage.py syncdb
    $ python manage.py runserver [port]
    
At this point auction_men is running at localhost on port 8000 or on your custom port if you specified it, so type

    localhost:8000
or

    localhost:8000/home
    
###Note for development
Auction-men provide the useful feature of email confirmation after you sign up. In order to enble this feature on development follow this instructions:

- You have to provide a verified `email host user` and an `email host password` in `settings.py`

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = '' # your host
    EMAIL_HOST_PASSWORD = '' # your password
    
- If you are running auctions_men on `localhost:8000` for example, you must change the `domain name` in django:

    - type `localhost:8000/admin'
    - in site administration panel, go to Sites
    - click on the only record and change `domain name` and `display name` to `localhost:8000`
     
ENJOY!!!