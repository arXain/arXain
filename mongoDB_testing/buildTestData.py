import json
import hashlib, sha3
import urllib
import feedparser
#from dateutil import parser as dateparser

if __name__=='__main__':

    output = []
    #url = 'http://export.arxiv.org/api/query?search_query=cat:hep-ex+OR+cat:hep-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=1000'
    url = 'http://export.arxiv.org/api/query?search_query=abs:the&sortBy=submittedDate&sortOrder=descending&start=0&max_results=1000'
    data = urllib.request.urlopen(url).read()
    feed = feedparser.parse(data)
    for entry in feed.entries:
        arxiv_hash  =  entry.id.split('/abs/')[-1]
        arx_title   =  entry.title
        arx_author  = [author.name for author in entry.authors] #entry.authors #'; '.join(author.name for author in entry.authors)
        arx_summary =  entry.summary
        all_categories = [t['term'] for t in entry.tags]
        arx_cat =  [x for x in all_categories]
        for link in entry.links:
            if link.rel == 'alternate':
                arx_url = link.href
        arx_date = arx_date = entry.published #dateparser.parse(entry.published)
        
        obj = {
        'title' : arx_title, 
        'authors': arx_author,
        'summary': arx_summary,
        'keywords': arx_cat,
        'category': arx_cat,
        'timestamp': arx_date,
        'contract': hashlib.sha3_256(arxiv_hash.encode()).hexdigest().decode("utf-8") ,
        'comments': hashlib.sha3_256(arx_url.encode()).hexdigest().decode("utf-8") ,
        'submitter': hashlib.sha3_256(arx_summary.encode()).hexdigest().decode("utf-8") ,
        'revision': arxiv_hash[-1]
        }
        output.append(obj)
    
    with open('testdata.json', 'w') as f:
        json.dump(output, f, sort_keys=True, indent=2)
    
    print("Done!")
