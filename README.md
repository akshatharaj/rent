# Rent

Rent is a django application that ingests json data about rental property leases and associated marketing source leads 
and provides insight about ROI from investments on those marketing sources

## Installation

### Make a new virtual environment

    $ virtualenv --no-site-packages --distribute ~/Code/env
    $ cd ~/Code/env
    $ . bin/activate
    $ pip install -U distribute

### Install rent and all its dependencies

    $ cd ~/Code/
    $ git clone https://github.com/akshatharaj/rent.git
    $ pip install requirements.txt

### Set up Database connections

    $ install postgres
    $ create a database to hold application data and create a user login with access to that database
    $ edit rent/settings.py to specify database connection parameters 

### Then run

    $ python manage.py syncdb
    $ python manage.py migrate
    $ python manage.py collectstatic

## Documentation

### Data ingestion

    badige (meaning rent in an language called Kannada) app provides a management command called *load_data_from_file*
    TO run it,
    python manage.py load_data_from_file /path/to/file

### Data Insight
    badige app provides a management command called *compile_results_from_db* to get a compilation of ROI on marketing investments
    TO run it,
    python manage.py compile_results_from_db <4 digit year> <quarter>

    Sample result:

    python manage.py compile_results_from_db 2013 2

    Q2 2013:
    - Apartments.com total leads: 1, signed leases: 0, total cost: $0.00, avg cost per lead: $0.00


    Q2 2013:
    - Apartment Guide total leads: 37, signed leases: 0, total cost: $1485.00, avg cost per lead: $40.14


    Q2 2013:
    - Resident Referral total leads: 6, signed leases: 1, total cost: $500.00, avg cost per lead: $83.33

