#!/usr/bin/python

import os
import string

get_time_command = "echo $(($(date +%s)/1000)) > current_time"

def foo():
    
    f = open("prev", 'r')
    for i in f:
        prev = int(i)
        break

    print("prev: ", prev)

    f = open('current_time', 'r')
    curr = 0
    for i in f:
        curr = int(i)
        break
    print("curr: ", curr)

    f.close()

    f = open('current_time', 'w')
    f.write(str(curr))
    f.close()

    t_diff = curr - prev
    command_to_run = "find /Users/dharmesh/dropbox -mmin -%d -type f -print > changed_files" % (t_diff)
    print("difference is: ", t_diff)
    print("running command: ", command_to_run)
    
    os.system(command_to_run)

    skydrive = "/Users/dharmesh/Skydrive"

    f = open('changed_files', 'r')
    prev_file_names = []
    for i in f:
        i = i[:-1]
        print("file is: ", i)
        file_names = i.split('/')
        path_created = ""
        for j in range(0, len(file_names)-1):
            if(file_names[j] == '.' or file_names[j] == "Users" or file_names[j] == "dharmesh" or file_names[j] == "dropbox"):
                continue
            if(file_names[j] not in prev_file_names):
                os.system("mkdir %s" % (skydrive+"/"+path_created+"/"+file_names[j]))
                prev_file_names.append(file_names[j])
                path_created += file_names[j]
        prefix_length = string.rfind(i, "/", 0, -1)
        prefix = i[23:prefix_length+1]
        print("copying %s to %s" % (i, skydrive+prefix))
        os.system("cp %s %s" % (i, skydrive+prefix))

foo()
