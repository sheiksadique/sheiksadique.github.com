function loadPost(postname, srcloc, loc)
{
    /*
     * loadPost(postname,srcloc, loc)
     * postname: name of the post you want to display
     * srcloc: location of the source files
     * loc: location or element where the post is to be displayed 
     */
    $(loc).load(srcloc+"/"+postname+".post");
}

function loadPost4mURL(loc)
{
    /*
     * loadPost4mURL(loc)
     * loc: location or element where the post is to be displayed
     */
    postname = (window.location.hash).split('#')[1];
    srcloc = (window.location.pathname).split('.')[0];
    loadPost(postname, srcloc, loc);
}
