import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from app import db
from app.models import FblGame
from app.utils import input_to_dictionary


# A generic class describing game attributes
class FblGameAttribute:
  date = graphene.types.datetime.DateTime()
  completions = graphene.Int()
  attempts = graphene.Int()
  pass_td = graphene.Int()
  thrown_int = graphene.Int()
  receptions = graphene.Int()
  receiving_td = graphene.Int()
  rushing_td = graphene.Int()
  caught_int = graphene.Int()
  sacks = graphene.Int()


class FblGameObject(SQLAlchemyObjectType):
  class Meta:
    model = FblGame
    interfaces = (graphene.relay.Node, )


# Arguments to create an FblGame
class CreateFblGameInput(graphene.InputObjectType, FblGameAttribute):
  """Arguments to create an FblGame"""
  pass


# Arguments to update an FblPlayer
class UpdateFblGameInput(graphene.InputObjectType, FblGameAttribute):
  """Arguments to update an FblGame"""
  id = graphene.ID(required=True)


# create an FblGame
class CreateFblGame(graphene.Mutation):
  # The game created by the mutation
  fbl_game = graphene.Field(lambda: FblGameObject)

  class Arguments:
    input = CreateFblGameInput(required=True)

  def mutate(self, info, input):
    data = input_to_dictionary(input)

    fbl_game = FblGame(**data)

    db.session.add(fbl_game);
    db.session.commit()

    return CreateFblGame(fbl_game=fbl_game)


# Update an FblGame
class UpdateFblGame(graphene.Mutation):
  # The game being updated
  fbl_game = graphene.Field(lambda: FblGameObject)

  class Arguments:
    input = UpdateFblGameInput(required=True)

  def mutate(self, info, input):
    data = input_to_dictionary(input)

    fbl_game = db.session.query(FblGame).filter_by(id=data['id'])
    fbl_game.update(data)
    db.session.commit()
    fbl_game = db.session.query(FblGame).filter_by(id=data['id']).first()

    return UpdateFblGame(fbl_game=fbl_game)