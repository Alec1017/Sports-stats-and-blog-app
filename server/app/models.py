from app import db

class FblGame(db.Model):
  __tablename__ = 'fbl_game'
  id = db.Column(db.Integer, primary_key=True)
  fbl_player_id = db.Column(db.Integer, db.ForeignKey('fbl_player.id'))

  date = db.Column(db.DateTime)
  completions = db.Column(db.Integer)
  attempts = db.Column(db.Integer)
  completion_percentage = db.Column(db.Integer)
  pass_td = db.Column(db.Integer)
  thrown_int = db.Column(db.Integer)
  receptions = db.Column(db.Integer)
  receiving_td = db.Column(db.Integer)
  rushing_td = db.Column(db.Integer)
  caught_int = db.Column(db.Integer)
  sacks = db.Column(db.Integer)


class FblPlayer(db.Model):
  __tablename__ = 'fbl_player'
  id = db.Column(db.Integer, primary_key=True)

  captain = db.Column(db.String(256))
  image = db.Column(db.String(256))
  wins = db.Column(db.Integer)
  losses = db.Column(db.Integer)
  differential = db.Column(db.Integer)
  role = db.Column(db.String(256))
  description = db.Column(db.String(256))
  games_played = db.Column(db.Integer)
  games = db.relationship('FblGame', order_by='FblGame.date')

  def __repr__(self):
    return '<FblPlayer %r>' % self.captain