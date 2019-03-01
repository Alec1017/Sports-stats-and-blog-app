import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from app import db
from app.models import FblPlayer
from app.utils import input_to_dictionary
from app.schema_fbl_game import CreateFblGameInput


# A generic class describing player attributes
class FblPlayerAttribute:
  player_id = graphene.ID()
  captain = graphene.String()
  image = graphene.String()
  wins = graphene.Int()
  losses = graphene.Int()
  differential = graphene.Int()
  role = graphene.String()
  description = graphene.String()
  games_played = graphene.Int()
  games = graphene.List(CreateFblGameInput)


class FblPlayerObject(SQLAlchemyObjectType):
  class Meta:
    model = FblPlayer
    interfaces = (graphene.relay.Node, )


# Arguments to create an FblPlayer
class CreateFblPlayerInput(graphene.InputObjectType, FblPlayerAttribute):
  """Arguments to create an FblPlayer"""
  pass


# Arguments to update an FblPlayer
class UpdateFblPlayerInput(graphene.InputObjectType, FblPlayerAttribute):
  """Arguments to update an FblPlayer"""
  id = graphene.ID(required=True)


# create an FblPlayer
class CreateFblPlayer(graphene.Mutation):
  # The player created by the mutation
  fbl_player = graphene.Field(lambda: FblPlayerObject)

  class Arguments:
    input = CreateFblPlayerInput(required=True)

  def mutate(self, info, input):
    data = input_to_dictionary(input)

    fbl_player = FblPlayer(**data)

    db.session.add(fbl_player);
    db.session.commit()

    return CreateFblPlayer(fbl_player=fbl_player)


# Update an FblPlayer
class UpdateFblPlayer(graphene.Mutation):
  # The player being updated
  fbl_player = graphene.Field(lambda: FblPlayerObject)

  class Arguments:
    input = UpdateFblPlayerInput(required=True)

  def mutate(self, info, input):
    data = input_to_dictionary(input)

    fbl_player = db.session.query(FblPlayer).filter_by(id=data['id'])
    print('#####################################')
    print(data)
    print('#####################################')
    fbl_player.update(data)
    db.session.commit()
    fbl_player = db.session.query(FblPlayer).filter_by(id=data['id']).first()

    return UpdateFblPlayer(fbl_player=fbl_player)
