from app.database.models import Tasks


class Interaction:
    table = Tasks

    @classmethod
    def post(cls, title, description='', done=False):
        cls.table.post(title=title, description=description, done=done)

    @classmethod
    def get_one_by_title(cls, title):
        return cls.table.get_one_by_title(title=title)

    @classmethod
    def get_all(cls, named):
        if named:
            return cls.table.get_all_by_title(named)
        return cls.table.get_all()

    @classmethod
    def delete_one_by_title(cls, title):
        return cls.table.delete_one_by_title(title=title)

    @classmethod
    def update_one_by_title(cls, title, new_title, description, done):
        return cls.table.update_one_by_title(
            title=title,
            new_title=new_title,
            description=description,
            done=done
        )
