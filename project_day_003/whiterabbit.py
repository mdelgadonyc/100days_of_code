# Day 3 Project: The Matrix Has You

print('''
8b,dPPYba,   ,adPPYba,  ,adPPYba,   
88P'   `"8a a8P_____88 a8"     "8a  
88       88 8PP""""""" 8b       d8  
88       88 "8b,   ,aa "8a,   ,a8"  
88       88  `"Ybbd8"'  `"YbbdP"'   
''')
print("Wake up neo...")
print("\tThe Matrix has you.\n\t\tFollow the white rabbit...\n")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

pill = input("Two pills have been left on your desk, one blue and the other red, which one do you take? Blue? Red? ")

if pill.lower() == 'blue':
    print("\nIt's 6:30AM. You wake up to the sound of your alarm. Time to get ready for work, Thomas Anderson. Game over.")
    exit()
elif pill.lower() == 'red':
    rabbit_hole = input("\nWhat you believe to be Reality slowly melts away. You feel a little like Alice in Wonderland trumbling down the rabbit hole. Do you wish to see how deep the hole goes? Yes? No? ")
if rabbit_hole.lower() == 'no':
    print("\nIt's 6:30AM. You wake up to the sound of your alarm. Time to get ready for work, Thomas Anderson. Game over.")
    exit()
if rabbit_hole.lower() == 'yes':
    print("\nYou arrive at what appears to be a digital training simulation. An agent appears as well. He begins moving toward you.")

agent = input("Do you engage him or do you run away? Engage? Run? ")
if agent.lower() == 'engage':
  print("\nYou and the agent exchange blows in an epic kung fu sequence. The agent outmatches you. The last words you hear him saying before fading to black are 'This is goodbye, Mr. Anderson'. Game over.")
  exit()
if agent.lower() == 'run':
  print("\nYou run in the opposite direction! You clash through a door and on the other side find yourself in a dark city alley. At the end of the alley a payphone is ringing. The agent rushes out through the door behind you.")

phone_call = input("Do you keeping running even though the agent is fast gaining on you or do you make a mad dash for the phone? Run? Phone? ")
if phone_call.lower() == 'run':
    print("\nThe agent catches up to you and fires point blank. The last words you hear are 'This is goodbye, Mr. Anderson'. Game over.\n")
    exit()
if phone_call.lower() == 'phone':
    print("\nYou make a mad dash for the phone, bringing the handset to your ear. The screeching sound of a distorted modem overtakes your senses. You find yourself back safe on a hovercraft ship with the crew of the Nebuchadnezzar. Morpheous, smiling, appears in front of you, 'Welcome back, Neo.'\n")