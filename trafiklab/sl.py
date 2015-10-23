import requests

from settings import key_plats,key_real


def sites(searchstring):

        url = "http://api.sl.se/api2/typeahead.json?key={key}&searchstring={searchstring}"
        #download page from trafiklab
        resp = requests.get(url.format(key = key_plats, searchstring = searchstring))
        return resp.json()['ResponseData']

def departures(siteid):

        url = "http://api.sl.se/api2/realtimedepartures.json?key={key}&siteid={siteid}&timewindow=60"

        resp = requests.get(url.format(key = key_real, siteid = siteid))


        return resp.json()['ResponseData']

def trains(siteid):
    trainlist=[]

    return   departures(siteid)['Trains']

def buses(siteid):
   buslist=[]

   return   departures(siteid)['Buses']


