# API-event-manager
API for manage events by types

# Python required modules 
Install via PIP
- bcrypt
- Flask
- Flask-Cors
- flask-swagger
- mariadb

# Create MariaDB database and table
CREATE DATABASE eventsDB;
CREATE TABLE events (
	id INT(11) NOT NULL AUTO_INCREMENT,
	type varchar(2) NOT NULL,
	description TEXT,
	event_date date NOT NULL,
	viewed boolean NOT NULL,
	managed boolean NOT NULL,
	PRIMARY KEY (id)
);

# Run the API in dev mode
flask --app main run --host=0.0.0.0 --debug


