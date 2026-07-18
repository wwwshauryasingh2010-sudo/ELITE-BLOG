from app import db

class Blog(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    name=db.Column(db.String(100) , nullable=False)
    blog=db.Column(db.Text , nullable=False)

#------------LEAVING HERE TODAY WITH THIS DATE [14/07/2026]
