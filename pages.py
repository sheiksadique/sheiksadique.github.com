#!/usr/bin/python

from xml.dom.minidom import *
import glob

def generateAllPages(templates='./templates/', destination='./_html/'):
    '''
    Function to generate all pages of the website
    '''
    print('The following files are being generated.')
    for p in glob.glob1(templates, '*.html'):
        print p
        generatePage(p, templates=templates, destination=destination)

def generatePage(page='index.html', templates='./templates/', destination='./_html/'):
    '''
    Generate Page by filling up the templates
    page: name of the page
    templates: location of templates folder
    destination: location of generated files
    '''
    pg = parse(templates+page)
    tempNodes = pg.getElementsByTagName('template')
    for tn in tempNodes:
        tp = getTemplate(tn.getAttribute('class'), templates=templates)
        tn.parentNode.replaceChild(tp, tn)
    f = open(destination+page, 'w')
    pg.writexml(f)
    f.close()
    return pg

def getTemplate(name='header', templates='./templates/'):
    '''
    Returns a node with the template html
    '''
    pg = parse(templates+name+'.tmpl')
    return pg.childNodes[0]

generateAllPages(destination='./')
