from app import db


class Tasks(db.Model):
    unique_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True)
    description = db.Column(db.String(1024), index=True)
    done = db.Column(db.Boolean, default=False)

    @classmethod
    def post(cls, title, description='', done=False):
        db.session.add(Tasks(title=title, description=description, done=done))
        db.session.commit()

    @classmethod
    def get_all(cls):
        return db.session.query(cls).all()

    @classmethod
    def get_one_by_title(cls, title):
        return db.session.query(cls).filter_by(title=title).first_or_404()

    @classmethod
    def get_all_by_title(cls, title):
        return db.session.query(cls).filter_by(title=title).all()

    @classmethod
    def delete_one_by_title(cls, title):
        record = cls.get_one_by_title(title)
        db.session.delete(record)
        db.session.commit()
        return record

    @classmethod
    def update_one_by_title(cls, title, new_title, description, done=False):
        record = cls.get_one_by_title(title)

        record.title = new_title
        record.description = description
        record.done = done

        db.session.commit()
        return record

    def __repr__(self):
       return "<Task({}, {}, {}, {})>".format(self.unique_id, self.title, self.description, self.done)


db.create_all()
