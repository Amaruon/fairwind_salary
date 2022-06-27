from application import App


if __name__ == '__main__':
    app = App('salary', '1podnano&')

    from models import Names, Project, Pms

    app.db.create_all()
    app.db.session.commit()
