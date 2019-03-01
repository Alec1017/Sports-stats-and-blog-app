from app import db
from app.models import FblGame, FblPlayer
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

# Schema objects

class FblGameObject(SQLAlchemyObjectType):
  class Meta:
    model = FblGame
    interfaces = (graphene.relay.Node, )

class FblPlayerObject(SQLAlchemyObjectType):
  class Meta:
    model = FblPlayer
    interfaces = (graphene.relay.Node, )



# create objects

class CreateFblPlayer(graphene.Mutation):
  class Arguments:
    captain = graphene.String(required=True)
    image = graphene.String()
    wins = graphene.Int()
    losses = graphene.Int()
    differential = graphene.Int()
    role = graphene.String()
    description = graphene.String()
    games_played = graphene.Int()
    games = graphene.List(FblGameObject)

  fbl_player = graphene.Field(lambda: FblPlayerObject)

  def mutate(self, info, captain, image, wins, losses, differential, role, description, games_played, games):
    fbl_player = FblPlayer(
      captain=captain,
      wins=wins,
      losses=losses,
      differential=differential,
      role=role,
      description=description,
      games_played=games_played,
      games=games
    )

    db.session.add(fbl_player);
    db.session.commit()

    return CreateFblPlayer(fbl_player=fbl_player)



# class CreateFblGame(graphene.Mutation):
#   class Arguments:
#     date = graphene.types.datetime.DateTime()
#     completions = grahphene.Int()
#     attempts = grahphene.Int()
#     completion_percentage = grahphene.Int()
#     pass_td = grahphene.Int()
#     thrown_int = grahphene.Int()
#     receptions = grahphene.Int()
#     receiving_td = grahphene.Int()
#     rushing_td = grahphene.Int()
#     caught_int = grahphene.Int()
#     sacks = grahphene.Int()



#   fbl_game = graphene.Field(lambda: FblGameObject)

#   def mutate(self, info, captain):

#     fbl_player = FblPlayer(captain=captain)

#     db.session.add(fbl_player)

# Graphene objects

class Query(graphene.ObjectType):
  node = graphene.relay.Node.Field()
  all_fbl_players = SQLAlchemyConnectionField(FblPlayerObject)
  all_fbl_games = SQLAlchemyConnectionField(FblGameObject)
  
class Mutation(graphene.ObjectType):
  create_fbl_player = CreateFblPlayer.Field()
  #create_fbl_game = CreateFblGame.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)