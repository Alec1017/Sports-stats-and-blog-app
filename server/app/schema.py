import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from app import schema_fbl_player, schema_fbl_game


class Query(graphene.ObjectType):
  node = graphene.relay.Node.Field()
  all_fbl_players = SQLAlchemyConnectionField(schema_fbl_player.FblPlayerObject)
  all_fbl_games = SQLAlchemyConnectionField(schema_fbl_game.FblGameObject)
  
class Mutation(graphene.ObjectType):
  create_fbl_player = schema_fbl_player.CreateFblPlayer.Field()
  update_fbl_player = schema_fbl_player.UpdateFblPlayer.Field()
  create_fbl_game = schema_fbl_game.CreateFblGame.Field()
  update_fbl_game = schema_fbl_game.UpdateFblGame.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)