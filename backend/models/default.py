from .db import db, ma


class Default(db.Model):
    __tablename__ = "test"
    
    id = db.Column("answer_id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    

    def __init__ (self, name):
        self.name = name

    def json(self):
        return {'id': self.id, 'name': self.name}
    
    def __repr__(self):
        return f"Answer ID:({self.id}, name: {self.name})"
    
    @classmethod
    def get_test_by_id(cls, id):
        return cls.query.filter(cls.id == id).first()
    

class DefaultSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Default
        session = db.session
        load_instance = True