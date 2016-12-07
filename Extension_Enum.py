import urllib2
import threading
import Queue
import urllib
import sys

threads = 5
target_url = sys.arv[1]
wordlist_file = sys.argv[2]
resume = None
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"

def construct_list(wordlist_file):
    fd = open(wordlist_file, "rb")
    raw_words = fd.readlines()
    fd.close()
    found_resume = False
    words = Queue.Queue()
    for word in raw_words:
        word = word.rstrip()
        if resume is not None:
            if found_resume:
                words.put(word)
            else:
                if word == resume:
                    found_resume = True
                    print "Resuming wordlist from: %s" % resume
        else:
            words.put(word)
    return words

def content_lookup(pooling, extensions=None):
    while not pooling.empty():
        attempt = pooling.get()
        attempt_list = []
        if "." not in attempt:
            attempt_list.append("/%s/" % attempt)
        else:
            attempt_list.append("/%s" % attempt)
        if extensions:
            for extension in extensions:
                attempt_list.append("/%s%s" % (attempt, extension))
        for brute in attempt_list:
            url = "%s%s" % (target_url, urllib.quote(brute))
            try:
                headers = {}
                headers["User-Agent"] = user_agent
                r = urllib2.Request(url, headers=headers)
                response = urllib2.urlopen(r)
                if len(response.read()):
                    print "[%d] => %s" % (response.code, url)
            except urllib2.URLError as e:
                if hasattr(e, 'code') and e.code != 404:
                    print "!!! %d => %s" % (e.code, url)
                pass


pooling = construct_list(wordlist_file)
extensions = [".html", ".php", ".bak", ".orig", ".inc"]
for i in range(threads):
    t = threading.Thread(target=content_lookup, args=(pooling,extensions,))
    t.start()
