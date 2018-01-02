"""
Snips info from rc.xml and converts it into easy to read notes.

ex. Input:  <keybind key="C-S-p">
                <action name="Execute">
                    <command>sh ~/pycharm-2017.3.1/bin/pycharm.sh</command>
                </action>
            </keybind>

    Output: Execute - sh ~/pycharm-2017.3.1/bin/pycharm.sh
                    K: Control + Shift + p
"""
# Super Word Search module
import re

# Regular Expressions
sec = re.compile("\<\/*keyboard\>")
bind = re.compile("\<\/*keybind\>*")
keys = re.compile('key=\s*"\S+">')
act = re.compile("\<\/*action\>*")
name = re.compile('key=\s*"\S+">')
comm = re.compile("\<\/*command\>")
comm_text = re.compile('\S')

# Reads the Openbox Settings file
with open("/home/matthew/.config/openbox/rc.xml") as f:
    content = f.readlines()

# Section switches
in_sec = False
in_bind = False
in_keys = False
in_act = False
in_name = False
in_comm = False
in_comm_text = False

# Clean Up

key_list = []


def strip_key(key):
    key = str(key)
    key = key[7:-4]
    return key


# Snip specific sections with relevant information
for line in range(len(content)):
    t = sec.findall(content[line])

    if t:  # if we find <keyboard> flip in_sec to TRUE, and vis-versa with </keyboard>
        in_sec = not in_sec
        # print("section flipped")
        # print(t)

    if in_sec:
        t = bind.findall(content[line])

        if t:
            in_bind = not in_bind
            # print("    bind flipped")
            # print("    " + str(t))

        if in_bind:
            k = keys.findall(content[line])
            a = act.findall(content[line])

            if k:
                in_keys = not in_keys
                # print("        keys flipped")
                k = strip_key(k) # reformats the key to be more readable
                key_list.append(k)
                # print("        " + k)

            if a:
                in_act = not in_act

            if in_act:
                n = name.findall(content[line])
                c = comm.findall(content[line])

                if n:
                    in_name = not in_name
                    # n = strip_name(n)
                    # name_list.append(n)

                if c:
                    in_comm = not in_comm

                if in_comm:
                    t = comm_text.findall(content[line])
                    # t = strip_comm(t)
                    # comm_list.append(t)


print(key_list)