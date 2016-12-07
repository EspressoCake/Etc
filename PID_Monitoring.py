import win32con
import win32api
import win32security
import wmi
import sys
import os

def PID_Identifier(pid):
    try:
        hproc = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION, False, pid)
        htok = win32security.OpenProcessToken(hproc, win32con.TOKEN_QUERY)
        privs = win32security.GetTokenInformation(htok, win32security.TokenPrivileges)
        priv_list = ""
        for i in privs:
            if i[1] == 3:
                priv_list += "%s|" % win32security.LookupPrivilegeName(None, i[0])
    except:
        priv_list = "N/A"
    return priv_list

def export_Data(message):
    fd = open("process_monitor_log.csv", "ab")
    fd.write("%s\r\n" % message)
    fd.close()

export_Data("Time,User,Executable,CommandLine,PID,Parent PID,Privileges")
c = wmi.WMI()
process_watcher = c.Win32_Process.watch_for("creation")
while True:
    try:
        initialized_Process = process_watcher()
        proc_owner = initialized_Process.GetOwner()
        proc_owner = "%s\\%s" % (proc_owner[0], proc_owner[2])
        create_date = initialized_Process.CreationDate
        executable = initialized_Process.ExecutablePath
        cmdline = initialized_Process.CommandLine
        pid = initialized_Process.ProcessId
        elder_ID = initialized_Process.ParentProcessId
        privileges = PID_Identifier(pid)
        process_log_message = "%s,%s,%s,%s,%s,%s,%s\r\n" % (create_date, proc_owner, executable,
                                                            cmdline, pid, elder_ID, privileges)
        print process_log_message
        export_Data(process_log_message)
    except:
        pass
