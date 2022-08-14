# Registration System using Python CGI, MySQL, and HTML

## Introduction

This is a registration system for a fictional company.
User can register their email, name.
After confirmation, user receives and SMS message with a thank you message.

# NGROK

NGrok was used to make the server publicly accessible.

# Docker

run `docker-compose up `to get the container running with the mysql database inside.

- Access the db inside the container with `docker exec -it <container_name> bash`
- `mysql -u root -p` to access the database
- type the password: 1234
- type `show databases;` to see the databases

- `use cs531;` to access the database:
- create a table named `users`:
  `create table users (user_id int not null auto_increment primary key, user_name varchar(255) not null, user_email varchar(255) not null, submission_date date );`
- show table structure:
  `describe users;`

# Running the application:

Ente the following file: registrationSystem-cs531/html/cgi-bin/confirm.py

1. change the token variable to you gmail password app token created in you gmail account.
2. change the email variable to your gmail email address.

`python -m http.server --cgi`

Complete each step on the registration.
Check you email for the SMS message.
