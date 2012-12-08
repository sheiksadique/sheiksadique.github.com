#!/usr/bin/python

from xml.dom.minidom import *
import glob

def generateAllPages(path='./src/pages/', templates='./src/templates/', destination='./_html/'):
    '''
    Function to generate all pages of the website
    '''
    print('The following files are being generated.')
    for p in glob.glob1(path, '*.html'):
        print p
        generatePage(p, path=path, templates=templates, destination=destination)

def generatePage(page='index.html', path='./src/pages/', templates='./src/templates/', destination='./_html/'):
    '''
    Generate Page by filling up the templates
    page: name of the page
    templates: location of templates folder
    destination: location of generated files
    '''
    pg = parse(path+page)
    #tempNodes = pg.getElementsByTagName('template')
    #for tn in tempNodes:
    #    tp = getTemplate(tn.getAttribute('class'), templates=templates)
    #    tn.parentNode.replaceChild(tp, tn)
    includeTemplate(pg, templates=templates)
    f = open(destination+page, 'w')
    pg.writexml(f)
    f.close()
    return pg

def includeTemplate(pg, templates='./src/templates/'):
    '''
    Include/replace html code from templates recursively
    pg: parse html page/node
    templates: location of template files
    '''
    tempNodes = pg.getElementsByTagName('template')
    for tn in tempNodes:
        tp = getTemplate(tn.getAttribute('class'), templates=templates)
        tn.parentNode.replaceChild(tp, tn)
    
    # Check for templates 
    tempNodes = pg.getElementsByTagName('template')
    if len(tempNodes) > 0:
        includeTemplate(pg, templates=templates)

    return pg


def getTemplate(name='header', templates='./src/templates/'):
    '''
    Returns a node with the template html
    '''
    pg = parse(templates+name+'.tmpl')
    return pg.childNodes[0]

if __name__=='__main__':
    generateAllPages(destination='./')
