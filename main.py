from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = 'captain'
    user.speciality = "research enginner"
    user.address = 'module_1'
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    user1 = User()
    user1.surname = "Dika"
    user1.name = "Vika"
    user1.age = 100
    user1.position = 'player'
    user1.speciality = "doing nothing"
    user1.address = 'module_2'
    user1.email = "vikadika@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user1)
    user3 = User()
    user3.surname = "Pupkin"
    user3.name = "Vasy"
    user3.age = 18
    user3.position = 'kok'
    user3.speciality = "cooking"
    user3.address = 'module_3'
    user3.email = "kokki@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user3)
    user2 = User()
    user2.surname = "Holl"
    user2.name = "Tom"
    user2.age = 20
    user2.position = 'doctor'
    user2.speciality = "helping"
    user2.address = 'module_3'
    user2.email = "doktom@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user2)
    db_sess.commit()
    #app.run()


if __name__ == '__main__':
    main()