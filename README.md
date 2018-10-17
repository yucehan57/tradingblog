# Trading Blog

Trading blog is a comprehensive-to-be blog that I have been 
working on for a while to improve my existing skills regarding
both python and django framework. The main reason this
blog is named Trading blog is mostly about my personal
liking towards finance as well as trading industry. Mid-term
goal of mine is to populate the blog with latest finance,
foreign exchange fluctuations, trading, as well as
economic related personal opinions. 




### Requirements

* Python 3.6+
* Django 2.1+

### Installation

Clone the repo, create virtual environment:

    $ git clone https://github.com/yucehan57/tradingblog.git
    $ virtualenv env
    $ source/env/bin/activate
    
Environment is set up. To proceed, you begin by making necessary migration

    $ python manage.py makemigrations
    $ python manage.py migrate
    
And, run the server:

    $ python manage.py runserver