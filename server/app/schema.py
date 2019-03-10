import graphene
from app.models import FblPlayer, FblGame

from app import schema_fbl_player, schema_fbl_game


class Query(graphene.ObjectType):
  node = graphene.relay.Node.Field()

  all_fbl_players = graphene.List(schema_fbl_player.FblPlayerObject)
  all_fbl_games = graphene.List(schema_fbl_game.FblGameObject)
  
  def resolve_all_fbl_players(self, info, **kwargs):
    return FblPlayer.query.all()

  def resolve_all_fbl_games(self, info, **kwargs):
    return FblGame.query.all()

  
class Mutation(graphene.ObjectType):
  create_fbl_player = schema_fbl_player.CreateFblPlayer.Field()
  update_fbl_player = schema_fbl_player.UpdateFblPlayer.Field()
  create_fbl_game = schema_fbl_game.CreateFblGame.Field()
  update_fbl_game = schema_fbl_game.UpdateFblGame.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)