function loadPost(postname, loc)
{
    /*
     * loadPost(postname, loc)
     * postname: name of the post you want to display
     * loc: location or element where the post is to be displayed 
     */
    $(loc).load("posts/"+postname+".post");
}

function loadPost4mURL(loc)
{
    /*
     * loadPost4mURL(loc)
     * loc: location or element where the post is to be displayed
     */
    postname = (window.location.hash).split('#')[1];
    loadPost(postname, loc);
}
