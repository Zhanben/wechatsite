# flask_site
a study project for flask

# install virtual env
1、virtualenv venv    
2、 .\venv\Scripts\activate

# install requirement
pip freeze | tee requirements.txt
pip install -r requirements.txt

# update database
python manager.py db init
python manager.py db migrate -m "initial migration"
python manager.py db upgrade





