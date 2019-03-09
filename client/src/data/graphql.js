import gql from 'graphql-tag';

export const PLAYERS = gql`
  {
    allFblPlayers {
      captain
      role
      description
      image
    }
  }
`;

export const STANDINGS = gql`
  {
    allFblPlayers {
      captain
      wins
      losses
      differential
    }
  }
`;