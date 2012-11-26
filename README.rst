Sadique Sheik's home page
=========================

The homepage is developed based on a template designed my Bryant Smith. Below
are the details of the template.

Design by Bryant Smith
http://www.bryantsmith.com
http://www.aszx.net
email: template [-at-] bryantsmith [-dot-] com
Released under Creative Commons Attribution 2.5 Generic.  In other words, do with it what you please; but please leave the link if you'd be so kind :)

Name       : An Ocean of Sky
Description: One column, with top naviation.  All divs, validations: XHTML Strict 1.0 & CSS
Version    : 1.0
Released   : 20081009

Template
========

Several modificaitons have been made to the original template to make life
easier. The directory structure is as follows.

  ::

    img/ -- Image directory
    styles/ -- css style sheet files
    src/ -- This is where the webpages under development are placed.
                  There are essentially two calsses of files.
                  /pages/ - .html : HTML page files.
                  /templates/ - .tmpl : reusable html code.

Any pages that are to be included should be named \*.html and placed in templates folder. You can use "<template class='templatename'/>" tag in your pages to use any of the reusable html in src/templates/\*.tmpl files.

Page generation
===============

To generate the final pages do the following.

  ::

    $./pages.py
