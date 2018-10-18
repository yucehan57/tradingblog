# Trading Blog

Trading blog is a comprehensive-to-be blog that I have been 
working on for a while to improve my existing skills regarding
both python and django framework. The main reason this
blog is named Trading Blog is mostly about my personal
liking towards finance as well as trading industry. Mid-term
goal of mine is to populate the blog with latest finance,
forex, trading, as well as
economics related personal opinions. 
Hopefully it will serve as a guidance for investors, traders, and/or
finance enthusiasts around the world as means to help them better
understand trends and fluctuations in the global market.




### Requirements

* Python 3.6+
* Django 2.1+

### Installation

Clone the repo, create virtual environment:

    $ git clone https://github.com/yucehan57/tradingblog.git
    $ virtualenv env
    $ source/env/bin/activate
    
Environment is set up. To proceed, you begin by making necessary migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate
    
And, run the server:

    $ python manage.py runserver
