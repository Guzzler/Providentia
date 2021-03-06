from app import db

class ImageData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(64), index=True, unique=True)
    classification = db.Column(db.String(120), index=True, unique=True)


    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3
    def __repr__(self):
        return '<ImageData %r>' % (self.name)
