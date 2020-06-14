var postformid;
var replybtnid;
var cmtext;
var talkid;
var abtnid;

function getids(postid){
  console.log(postid)
  postformid = '#postform'+postid
  replybtnid = '#replybtn'+postid
  cmtext = '#comment-text'+postid
  talkid = '#talk'+postid

  $(postformid).one('submit', function(event){
      event.preventDefault();
      console.log(event)
      console.log("form submitted!")  // sanity check
      create_comment(postid);
  });
}

// AJAX for posting
function create_comment(postid) {
    console.log("create comment is working!") // sanity check
    console.log(postid)
    console.log(talkid)
    $.ajax({
        url : "create_comment/"+postid, // the endpoint
        type : "POST", // http method
        data : { the_comment : $(cmtext).val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $(cmtext).val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            $(talkid).prepend(
              "<div class='col-1 p-0'><img class='rounded w-100 h-75' src='"+ json.image +
              "'></div><div class='col-9 p-3'><p class='h5'>" +json.user +
              " &nbsp <span class='h6 text-muted'>" + json.created +
              "</span></p><p class='h5 lead'>"+ json.text +
              "</p></div><div class='col-1 px-3 py-4'><p>"+ json.likes +
              "<i class='fa fa-thumbs-o-up fa-lg float-right' area-hidden='true'></i></p></div><div class='col-1 px-3 py-4'><p>"+ json.dislikes +
              "<i class='fa fa-thumbs-o-down fa-lg float-right' area-hidden='true'></i></p></div>");
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};


function upvotecomment(postid, commentid, votes_total){
  console.log(postid,commentid)
  abtnid = '#abtn'+commentid
  upvotingcmt = '#upvotingcomment'+commentid
  $(upvotingcmt).one('submit', function(event){
      event.preventDefault();
      console.log(event)
      console.log("form submitted!")  // sanity check
      upvotecomment(postid, commentid, votes_total);
  });
}

// AJAX for posting
function upvotecomment(postid, commentid, votes_total) {
    console.log("upvote comment is working!") // sanity check
    console.log(postid)
    console.log(commentid)
    console.log(votes_total)
    totalupvotes = '#total_upvotes'+commentid
    $.ajax({
        url : "upvotecomment/"+postid+"/"+commentid, // the endpoint
        type : "POST", // http method
        // data : { the_comment : $(cmtext).val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            // $(cmtext).val(''); // remove the value from the input
            votes_total += 1;
            console.log(json); // log the returned json to the console
            $(totalupvotes).text(votes_total);
            // $(talkid).prepend();
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};


$(function() {
    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});
