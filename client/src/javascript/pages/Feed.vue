<template>
<div class="container">
  <div class="feed tweets">
    <a class="feed__timeline twitter-timeline" href="https://twitter.com/FBLWBL2019?ref_src=twsrc%5Etfw" data-chrome="nofooter noborders">Tweets by FBLWBL2019</a>
  </div>
</div>
</template>

<script>
  export default {
    created() {
      let feed = document.createElement('script');
      feed.setAttribute('src', 'https://platform.twitter.com/widgets.js');
      feed.setAttribute('charset', 'utf-8');
      document.head.appendChild(feed);
    }
  }
</script>
