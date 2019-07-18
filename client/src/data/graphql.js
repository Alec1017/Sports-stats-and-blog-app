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
          ip
          er
          r
          pitching_k
          pitching_bb
          sv
          pitching_wins
          pitching_losses
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
          division
          facebook
          twitter
          instagram
        }
      }
    }
  }
`;

export const HOMEPAGE = gql`
  {
    homepage(uid: "homepage", lang:"en-us") {
      about_section_one
      about_section_two
      images {
        featured_image
        caption
      }
      livestream_link
    }
  }
`;

export const STANDINGS = gql`
  {
    standings(uid: "standings", lang:"en-us") {
      divisions
    }
  }
`;