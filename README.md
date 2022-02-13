# Django_Authentication

Follow Steps:

# Python

First Step:
    
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
        
Second Step:

    Now, just rename the .env.sample file to .env and run:    

Third Step:

    - python3 manage.py migrate (migrates to database)
    
    - python3 manage.py createsuperuser (create a superuser to access django admin painel)
    
    insert username, email and password
    
Fourth Step:

    run a command: python3 manage.py runserver
    
    access url http://127.0.0.1:8001/swagger copy and paste on url
    


If do you have docker-compose you could you command:

    docker-composer up -d --build


#  Django_Authentication


# Swagger
<img src="/assets/swagger.png" >

# Insomnia
<img src="/assets/insomnia.png" >
