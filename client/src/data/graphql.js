import gql from 'graphql-tag';

// Removes edges and node from the structure
export const cleanCollection = (collection) => {
  let docs = [];
    for (const doc of collection.edges) {
      docs.push(doc.node);
    }
    return docs;
}


export const WBLPLAYERS = gql`
  {
    allWbl_players {
      edges {
        node {
          role
          description
          games_played
          captain
          profile_picture 
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