**Postgresql Installation:**
<br>
Ref Link: [https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-16-04]()
<br><br>
`sudo apt-get update`
<br><br>
`sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib`
<br><br>
`sudo -u postgres psql`
<br><br>
`CREATE DATABASE postgresdb; #postgresdb will be your database name`
<br><br>
`GRANT ALL PRIVILEGES ON DATABASE postgresdb TO postgres;`
<br><br>
`CREATE USER postgres WITH PASSWORD 'password';`
<br><br><br>
**Install Django within a Virtual Environment**
<br><br>
`sudo apt-get install python3-pip`
<br><br>
`sudo pip3 install virtualenv `
<br><br>
`virtualenv envOne`   `#It will create virtual environemnt`
<br><br>
`source envOne/bin/activate`
<br><br>
`pip install -r req.txt` `#Install all the dependency`
<br><br><br>
**Project Setups**
<br><br>
`take git pull using` `git pull gitlink`
<br><br>
`cd tijori`
<br><br>
`python manage.py migrate`
<br><br>
`python manage.py shell`
<br><br>
`from api import migratedb`   `After getting Success message quit the shell terminal`
<br><br>
`python manage.py runserver`
<br><br>
`Open Browser Chrome or Firefox or anything`
<br><br>
`GET  http:/127.0.0.1:8000/api/company/<fincode>/current_price/`  `Provide Fincode in url bar`
<br>
`GET  http:/127.0.0.1:8000/api/company/<fincode>/historical_prices/`   `Provide Fincode in url bar`
