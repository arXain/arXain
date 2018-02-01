App2 = {
  web3Provider: null,
  contracts: {},

  init: function() {
    // Load paper.
    $.getJSON('src/papers.json', function(data) {
      var articleRow = $('#articleRow');
      var articleTemplate = $('#articleTemplate');

      for (i = 0; i < data.length; i ++) {
        // Pin the data locally to speed up loading and future network distribution
        // We can change this last part to be ...=/ipfs/"+data[i].corpusID"/recursive=true
        articleTemplate.find('.article-title').text(data[i].title);        
        articleTemplate.find('.article-title').attr('href', "http://localhost:8080/ipns/"+data[i].submitter+"/"+data[i].doi+"/"+data[i].doi+".pdf");
        articleTemplate.find('.article-authors').text(data[i].authors);
        articleTemplate.find('.article-submitter').text(data[i].submitter);
        articleTemplate.find('.article-tags').text(data[i].tags);
        articleTemplate.find('.article-doi').text(data[i].doi);
        articleTemplate.find('.article-abstract').text(data[i].abstract);
        articleTemplate.find('.article-date').text(data[i].timestamp);

        articleRow.append(articleTemplate.html());
      }
    });
  },
};

$(function() {
  $(window).load(function() {
    App2.init();
  });
});

