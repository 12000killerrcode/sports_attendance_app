from app import app, db
from app.models import User, Performance, Target, Player, Post, Coaching, EditPlayer


#add database instance and models to a flask sehell session
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Performance=Performance, Target=Target, Player=Player, Post=Post, Coaching=Coaching, EditPlayer=EditPlayer   )






