# HungryMe
HungryMe is an online food suggestion website which suggests to people what they want to eat!

Recommendations using search box. However, if you have no clue about the dish you really want for today, the filters can categorize the suggestion such as cuisines, ingredients, desired nutrition or even the food allergies. The visitors can rate and leave a comment about how good the suggestion of the suggested dish is.

## Project Documents
- [Project Proposal](https://docs.google.com/document/d/1DW7tv5Bpf5_tJoBKPRP4io66zMDQzeJHZ7YWnl435PU/edit?usp=sharing)
- [User Stories](../../wiki/User-Stories)<br>

# How to Install and Runserver (as a Developer)

1. Clone this project repository to your local machine
    ````
    git clone https://github.com/jaybjackie/HungryMe.git
    ````
2. Go to  this repository directory<br>
   
   for `MacOS/Linux`
   ````
   cd HungryMe
   ````
   
    
3. Install required packages.

    ````
    pip install -r requirements.txt
    ````

4. Modify `sample.env` by the following lines:

    To create SECRET KEY
    ```
    python -c 'from django.core.management.utils import get_random_secret_key;print(get_random_secret_key())'
    ```

    Put the SECRET KEY in .env file

    ```
    SECRET_KEY = 'YOUR-SECRET-KEY'
    DEBUG = False
    ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']
    ```

5. Migrate the database.

    for `MacOS/Linux`
    ````
    python manage.py migrate
    ````

6. Importing data from `data.json`.
    ````
    python manage.py loaddata data.json
    ````
7. Run the server.
 
   for `MacOS/Linux`
   ````
   python manage.py runserver
   ````
 
 Go to the app:
[http://localhost:8000/](http://localhost:8000/)