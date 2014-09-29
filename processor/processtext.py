# -*- coding: utf-8 -*-
'''
Created on 15/06/2013
@author: Marcos Aguayo
'''

import re
import webbrowser

class ProcessText(object):
    web = ['sitio web', 'web', 'pagina web', 'página web']
    url_visit = "";
    isWeb = False;

    def __init__(self, *args, **kwargs):
        print "Llamado a procesar"
        
    def set_orden(self, command):
        self.command = command
        return self.process()
    
    
    def getURL(self):
        regex = re.compile("([0-9A-Za-z]{2,}\.[0-9A-Za-z]{2,3}\.[0-9A-Za-z]{2,3}|[0-9A-Za-z]{2,}\.[0-9A-Za-z]{2,3})$")
        web = regex.findall(str(self.command))
        web = str(web)
        web = web.replace("['", "")
        web = web.replace("']", "")
        return web
    
    # Checks if the phrase is a question. Normally it contains a "?".
    def isQuestion(self):
        if "?" in self.command :
            return True
        else:
            return False
    
    def process(self):
        self.commandList = self.command.split();
        
        for word in self.commandList:
            print word
        
        # If it's a question
        if self.isQuestion():
            return 'Es una pregunta'
        else:
            # If there is a domain or URL on command
            if self.getURL() != '':
                self.url_visit = "http://%s" % self.getURL()
                print self.url_visit
                webbrowser.open_new(self.url_visit)
                return "Llendo a %s" % self.url_visit
        