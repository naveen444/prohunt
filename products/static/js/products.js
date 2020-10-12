var upvotingproduct,product;

function upvoteproduct(productid){
  console.log(productid)
  upvotingproduct = '#upvotingproduct'+productid

  $(upvotingproduct).one('submit', function(event){
      event.preventDefault();
      console.log(event)
      console.log("form submitted!")  // sanity check
      upvotingproduct(productid);
  });
}

// AJAX for posting
function upvotingproduct(productid) {
    console.log("upvoting product is working!") // sanity check
    console.log(productid)
    var i = document.getElementsByName('pitag'+productid)
    var product = '#product'+productid
    // errordiv = '#error'+commentid

    $.ajax({
        url : "upvote/"+productid, // the endpoint
        type : "POST", // http method

        // handle a successful response
        success : function(json) {
          console.log("success");
          if (json.result == 'upvoted') {
            console.log('upvoted');
            // $(i).toggleClass("far fas")
            console.log(json.votes_total); // log the returned json to the console
            $(product).text(json.votes_total);
          }
          else if (json.result == 'deleted') {
            console.log("deleted");
            // $(i).toggleClass("fas far")
            console.log(json.votes_total); // log the returned json to the console
            $(product).text(json.votes_total);
          }
          else {
            console.log('error');
            alert('error');
            // $(errordiv).fadeIn();
            // $(errordiv).prepend(
            //   "<p class='h5 lead text-danger'>"+ json.error + "</p>");
            // setTimeout(function() {
            //   $(errordiv).fadeOut('fast',function(){
            //     $(errordiv).empty();
            //   });
            // }, 4000);
          }
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log('error');
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
