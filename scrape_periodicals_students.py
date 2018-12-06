#coding: utf-8
#2018.10

import requests
import dataset
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_vids(req_id, tablename):
    ''' fill out codes for getting volume ids of a periodical.
    1.scrape volume ids
    2.put them into table of 'urls_title_req_id' in sql database.'''

    return v_ids

def scrape_mids_in_js(top_id):
    ''' fill out codes for getting the children ids of volume ids in interactive javascript codes
    1. let internet browser work on the top url
    2. get all volume ids
    3. let browser being clicked on a volume of periodical to unfold the childeren ids pages.
    4. get the children ids and save them to a output file.
    5. let browser being folded.
    6. close the browser
    7. return the output filename which holds the ids and volume titles'''

def make_vid_mid_title(infn):
    ''' fill out codes for making volume id and article ids and title pairs
    1. open the file holding the data
    2. parse them
    3. make them into (vid, mid, title) which is a tuple data
    4. return the tuple list. '''

def put_vid_mid(base_url, vid_mid_list):
    ''' fill out codes for puting the ids and title to table and article body
    1. get vid, article id(mid) from vid_mid_list
    2. for every mid do below
    3.      put vid, mid, and title to table
    3.      call scrape_article(..., mid) to get an article body and save it to table.
    4. return to finish '''

def scrape_article(base_url, article_id):
    ''' fill out codes for scraping article body and putting them to db.
    1. get an article page
    2. get every element to save
    3. insert them to db table.
    4. return to finish '''


if __name__ == "__main__":
    # global variables: db, base_url, top_id, ids_table, article_table
    db = dataset.connect('sqlite:///data/periodicals.db')
    base_url = 'http://db.history.go.kr/id/'
    #top_id = 'ma_013'
    import sys
    top_id = sys.argv[1] # ma_013, ma_014,...whatever if available in base_url/top_id
    ids_table = 'urls_title_%s' %top_id
    article_table = 'article_body_%s' %top_id

    scrape_vids(top_id, ids_table)
    id_fn=scrape_mids_in_js(top_id)
    ids_title = make_vid_mid_title(id_fn)
    put_vid_mid(base_url, ids_title)

