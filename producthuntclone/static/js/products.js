var upvotingproduct,product,upbutton;

function upvoteproduct(productid){
  console.log(productid)
  upvotingproduct = '#upvotingproduct'+productid
  upbutton = '#upbutton'+productid

  $(upvotingproduct).one('submit', function(event){
      event.preventDefault();
      console.log(event)
      console.log("form submitted!")  // sanity check
      upvotingp(productid);
  });
}

// AJAX for posting
function upvotingp(productid) {
    console.log("upvoting product is working!") // sanity check
    console.log(productid)
    product = '#product'+productid

    $.ajax({
        url : "products/upvote/"+productid, // the endpoint
        type : "POST", // http method

        // handle a successful response
        success : function(json) {
          console.log("success");
          if (json.result == 'upvoted') {
            console.log('upvoted');
            $(upbutton).toggleClass("btn-outline-custom btn-outline-dark")
            console.log(json.votes_total); // log the returned json to the console
            $(product).text("upvoted \xa0\xa0\xa0"+json.votes_total);
          }
          else if (json.result == 'deleted') {
            console.log("deleted");
            $(upbutton).toggleClass("btn-outline-dark btn-outline-custom")
            console.log(json.votes_total); // log the returned json to the console
            $(product).text("upvote \xa0\xa0\xa0"+json.votes_total);
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
