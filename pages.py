#!/usr/bin/python

from lxml import etree
import glob

def generateAllPages(path='./src/pages/', templates='./src/templates/',
                     posts='./posts/', destination='./_html/'):
    '''
    Function to generate all pages of the website
    '''
    print('The following files are being generated.')
    for p in glob.glob1(path, '*.html'):
        print p
        generatePage(p, path=path, templates=templates, posts=posts,
                     destination=destination)

def generatePage(page='index.html', path='./src/pages/',
                 templates='./src/templates/', posts='./posts/',
                 destination='./_html/',):
    '''
    Generate Page by filling up the templates
    page: name of the page
    templates: location of templates folder
    destination: location of generated files
    '''
    pg = etree.parse(path+page).getroot()
    includeTemplate(pg, templates=templates)
    for nd in pg.findall('.//{'+pg.nsmap[None]+'}postListBox'):
        listPosts(nd, posts=posts)
    with open(destination+page, 'w') as f:
        f.write(etree.tostring(pg, pretty_print=True))
    return pg

def includeTemplate(pg, templates='./src/templates/'):
    '''
    Include/replace html code from templates recursively
    pg: parse html page/node
    templates: location of template files
    '''
    tempNodes = pg.findall('.//{'+pg.nsmap[None]+'}template')
    for tn in tempNodes:
        tp = getTemplate(tn.get('class'), templates=templates)
        tn.getparent().replace(tn, tp)
    
    # Check for templates 
    tempNodes = pg.findall('.//{'+pg.nsmap[None]+'}template')
    if len(tempNodes) > 0:
        includeTemplate(pg, templates=templates)

    return pg

def getTemplate(name='header', templates='./src/templates/'):
    '''
    Returns a node with the template html
    '''
    pg = etree.parse(templates+name+'.tmpl')
    return pg.getroot()

def listPosts(pg, posts='./posts/'):
    '''
    Add all posts to the list.
    pg: node containing the template where posts are to be included
    posts: Location where posts are found
    '''
    print('The following posts are being listed.')
    node = etree.XML("<div class='postListBox'><div><ul /></div></div>")
    lst = node.findall('.//ul')[0]
    for p in glob.glob1(posts, '*.post'):
        print p
        lnk = etree.XML('<a />')
        pst = etree.parse(posts+p).getroot()
        for div in pst.findall('.//div'):
            if div.get('class') == 'contentTitle':
                nd = div.findall('.//a')[0]
                lnk.set('href', '#'+nd.get('id'))
                lnk.set('onclick', 
                        "loadPost('{0}', '#post-container')".format(
                            nd.get('id')))
                lnk.text = nd.text
        itm = etree.XML('<li />')
        itm.append(lnk)
        lst.append(itm)
    pg.getparent().replace(pg, node)
    return


if __name__=='__main__':
    generateAllPages(destination='./')
