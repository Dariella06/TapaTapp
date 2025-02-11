from flask import Flask, request, jsonify

class User:
    def __init__(self, id, username, password, email=""):
        self.id=id
        self.username=username
        self.password=password
        self.email=email

listUsers= [
    User(1,"usuari1", "12345", "prova@gmail.com"),
    User(2,"user2", "123", "user2@proven.cat"),
    User(3,"admin","12","admin@proven.cat"),
    User(4,"admin2","12"),
    User(5,"Dariella","2006","dariella@gmail.com")
]

