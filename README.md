//SERVER

    cd server
    virtualenv env
    source env/bin/activate
    
    pip install -r requirements.txt
    python app.py

//CLIENT
    cd client
    npm install
    npm run serve

    http://localhost:8080
