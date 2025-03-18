from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    name = input()
    #db_session.global_init("db/mars_explorer.db")
    db_session.global_init(name)
    db_sess = db_session.create_session()
    user = db_sess.query(User).first()
    for user in db_sess.query(User).filter(User.address.like("module_1")):
        print(user)

    #app.run()


if __name__ == '__main__':
    main()