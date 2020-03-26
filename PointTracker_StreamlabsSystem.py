# Imports

import csv

# Script information

ScriptName = "PointTracker"
Website = ""
Description = "!pt functionality to spend points on big ticket items"
Creator = "Kutsu Shita"
Version = "1.0.0.0"

# Variables

chairman = 'KutsuSheeta'
lines = []

def Init():
    with open('Services\Scripts\Channel-Point-Tracker\Tracked.txt') as tracked_file:
        reader = csv.reader(tracked_file)
        lines = list(reader)
    return

def Execute(data):
    if data.GetParam(0) != Command or Parent.IsOnUserCooldown(ScriptName, Command, data.User):
        return

    else:
        user_name = data.user_name

        if isinstance(data.GetParam(1), int):
            pt_num = data.GetParam(1)

            if pt_num >= 0 and pt_num < len(lines):
                pt_name = lines[pt_num][0]
                pt_desc = lines[pt_num][1]
                pt_points = lines[pt_num][2]
                pt_times_met = lines[pt_num][3]

                if isinstance(data.GetParam(2), int) and user_name == chairman:
                    pt_substract = data.GetParam(2)
                    pt_points -= pt_substract

                    if pt_points <= 0:
                        send_message('Challenge met! Looks like we get to enjoy "' + pt_name + '"...')
                        pt_points = 200000
                        lines[pt_num][3] += 1
                    
                    else:
                        send_message('"' + pt_name + '" has ' + pt_points + ' points left')
                        
                    lines[pt_num][2] = pt_points
                    with open('Services\Scripts\Channel-Point-Tracker\Tracked.txt') as tracked_file:
                        writer = csv.writer(tracked_file)
                        writer.writerows(lines)
                    return
                
                else:
                    send_message('Challenge: "' + _pt_num + ' - ' + pt_name + '"; ' + pt_desc + ' | Points left: ' + pt_points + ' | Times met: ' + pt_times_met)
                    return

            else:
                send_message('Sorry ' + user_name + ', the number provided (' + pt_num + ') does not have anything associated with it.')
                return

        else:
            send_message(user_name + ', that\'s not how this command works, you boob! !pt [some number]')
            return           

        if user_name != chairman:
            Parent.AddUserCooldown(ScriptName, Command, data.User, 30)

        return

def Tick():
    return

def send_message(message):
    return Parent.SendStreamMessage(message)

def log(message):
    Parent.Log(Command, message)
    return