# E Shop
## Steps to follow 
1.  Clone repository
2.  Create Virtualenv 
        ```virtualenv YOUR_VIRTUAL_ENV_NAME ```
    
3.  Activate virtual environment
        Command Prompt
            ``` YOUR_VIRTUAL_ENV_NAME\Scripts\activate.bat ```
        Power Shell
            ``` YOUR_VIRTUAL_ENV_NAME\Scripts\activate ```
        UNIX/Linux/Mac Terminal
            ``` source YOUR_VIRTUAL_ENV_NAME\bin\activate ```
5.  Install dependencies (Supporting Packages)
        Either install individual packages
            Command (In virtual environment):
            ``` pip install PACKAGE_NANE ```
        or install all packages at once from requirements.txt
            Command (In virtual environment):
            ``` pip install -r requirements.txt ```
            NOTE: This Command will install all the supporting packages listed in `requirements.txt` files
            
7.  Create Super User to access admin panel or use the development database.
        `username : admin`
        `password : 123456`
        To create super admin run command, 
        Command Prompt (In virtual environment)
            ```python manage.py createsuperuser ```
        complete the registration of super user by adding username and password.
        
9.  Run Migrations
        1. makemigrations: This Command will detect all the changes throughout the project model files
            Command Prompt (In virtual environment):
           ``` python manage.py makemigrations ```
        2. migrate : This Command will add new changes to database.
            Command Prompt (In virtual environment):
    ``` python manage.py migrate ```
10.  Run Server
        Command Prompt (In virtual environment):
        ```python manage.py runserver   ```
