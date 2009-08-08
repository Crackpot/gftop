#!/usr/bin/python

# Download pictures from PPPerson @ bbs.sjtu.edu.cn

import re
import os
from urllib  import ContentTooShortError
from urllib2 import URLError
import urllib, urllib2

def requestURL( url, datas, headers = None ) :
    """Request a url"""
       
    if not headers :
        headers = { 'User-Agent' : 'Mozilla/3.0' }
    # request
    req = urllib2.Request( url, datas, headers )
    # open url
    try :
        res = urllib2.urlopen( req )
    except URLError, e :
        if hasattr( e, 'reason' ) :
            print "Failed to reach server: ", e.reason
        elif hasattr( e, 'code' ) :
            print "Can't fulfill the requset: ",e.code
    else :
        pass #print "Requset is successful\n"

    return res

def getSubjectsURL( cmpPattern ) :
    """Get the url of subjects"""

    board_url = 'http://bbs.sjtu.edu.cn/bbstdoc'

    # baord
    data = { 'board' : 'PPPerson' }
    datas = urllib.urlencode( data )

    # get a response
    res = requestURL( board_url, datas )

    # create a compiled regular expression
    #cmpPattern = re.compile(r'<a href=bbstcon\?(.*?)>')
     
    # get the url list of titles
    subjectsURL = cmpPattern.findall( res.read() )

    return subjectsURL

def getImagesURL( url, cmpPattern ) :
    """Return the images url according to corresponding subject url"""

    # get the url of subject
    subject_url = 'http://bbs.sjtu.edu.cn/bbstcon'
    # get datas
    datas = url

    # request and get a response
    res = requestURL( subject_url, datas )
     
    # create a compiled pattern to find urls of images
    #cmpPattern = re.compile( r'<IMG\sSRC="(.*?)"\s>', re.I )

    # get the urls of images
    imagesURL = cmpPattern.findall( res.read() )

    # delete the repeated images
    sets = set( imagesURL )
    imagesURL = []
    for item in sets :
        imagesURL.append( item )

    return imagesURL

def downloadImage( imageURL, subID ) :
    """Download images"""

    # image url
    image_url = 'http://bbs.sjtu.edu.cn' + imageURL

    # create the directory to store images
    # if not os.path.exists( './download' ) :
    try :
        os.makedirs( './download/' + subID )
    except OSError :
        pass
        #print "Failed to create directories"

     
    # get filename of image
    filename = 'download/' + subID + '/' + imageURL.split( '/' )[-1]

    # clear the cache that may have been built up
    # by previous calls to urlretrieve()
    urllib.urlcleanup()
     
    # retrieve the image
    try :
        urllib.urlretrieve( image_url, filename )
    except ContentTooShortError :
        print "The data available was less than that of expected"
        print "Downloading file %s was interrupted" \
                        % os.path.basename( filename )
    else :
        # get the size of file
        size = os.path.getsize( filename ) / 1024
        print ">>>File %s (%s Kb) was done..." % ( filename, size )


if __name__ == '__main__' :
   
    # create compiled regular expression pattern
    findSubjectsPattern = re.compile( \
                    r'<td>(\d+)<td>.*?<a\shref=bbstcon\?(.*?)>', re.I | re.DOTALL )
    findImagesPattern   = re.compile( r'<IMG\sSRC="(.*?)"\s>', re.I )

    # get subjects' url list
    subjectsList = getSubjectsURL( findSubjectsPattern )

    print "Downloading begins...\n"

    filecount = 1

    for i in range( len( subjectsList ) ) :
        # get images url list
        print "\nSubject %s begins..." % subjectsList[i][0]
        imagesList = getImagesURL( subjectsList[i][1], findImagesPattern )
        # download all iamges
        for j in range( len(imagesList) ) :
            downloadImage( imagesList[j], subjectsList[i][0] )
            filecount += 1

    print "\nAll downloads were done"
    print "%d files were downloaded totally\n" % filecount