import gql from 'graphql-tag';

// Removes edges and node from the structure
export const cleanCollection = (collection) => {
  let docs = [];
    for (const doc of collection.edges) {
      docs.push(doc.node);
    }
    return docs;
}

export const GETWBLPLAYER = gql`
  query allWbl_players($uid: String!) {
    allWbl_players(uid: $uid) {
      edges {
        node {
          _meta {
            uid
          }
          role
          description
          captain
          profile_picture 
          wins
          losses
          batting_direction
          throw_direction
          age
          height
          status
          debut
          awards
          championship_titles
          h
          ab
          one_b
          two_b
          three_b
          hr
          hbp
          bb
          rbi
          k
          sb
          outs
        }
      }
    }
  }
`;


export const WBLPLAYERS = gql`
  {
    allWbl_players {
      edges {
        node {
          _meta {
            uid
          }
          role
          description
          captain
          profile_picture 
          wins
          losses
        }
      }
    }
  }
`;

export const HOMEPAGE = gql`
  {
    homepage(uid: "homepage", lang:"en-us") {
      images {
        featured_image
      }
    }
  }
`;