# API-event-manager
<h3>API for manage events by types</h3>
<p>The default por for the API is 5000</p>


# Python required modules 
Install via PIP
- Flask
- Flask-Cors
- flask-swagger
- mariadb

# Create MariaDB database and table
<code>CREATE DATABASE eventsDB;</code>
<br>
<code>CREATE TABLE events (
id INT(11) NOT NULL AUTO_INCREMENT,
type varchar(2) NOT NULL,
description TEXT,
event_date date NOT NULL,
viewed boolean NOT NULL,
managed boolean NOT NULL,
deleted boolean NOT NULL,
PRIMARY KEY (id)
);</code><br>

# Documentation
<p>The endpoints documentation will be described in the URL: <a href="localhost:5000/spec">swagger</a></p>

# Run the API in dev mode
flask --app main run --host=0.0.0.0 --debug


