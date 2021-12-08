import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

operation = input()
pseudo_random_number = int(input())

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

rotors = []

for i in range(3):
    rotor = input()
    rotors.append([char for char in rotor])
message = input()
msg_chars = [char for char in message]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

def caesar_encoded(string):
    caesared_msg_chars = []
    for i in range(0,len(string)):
        caesared_msg_chars.append(alphabet[(alphabet.index(msg_chars[i]) + i + pseudo_random_number) % len(alphabet)])
    return caesared_msg_chars

def caesar_decoded(string):
    caesared_msg_chars = []
    for i in range(0,len(string)):
        caesared_msg_chars.append(alphabet[(alphabet.index(msg_chars[i]) - i - pseudo_random_number) % len(alphabet)])
    return caesared_msg_chars

#rotor-coding
message_final = [None] * len(message)
if operation == "ENCODE":
    caesared_msg_chars = caesar_encoded(message)
    for i in range(0,3):
        for charIndex in range(len(message_final)):
            message_final[charIndex] = rotors[i][alphabet.index(caesared_msg_chars[charIndex])]
        caesared_msg_chars = message_final
else:
    for i in range(2,-1,-1):
        for charIndex in range(len(message_final)):
            message_final[charIndex] = alphabet[rotors[i].index(msg_chars[charIndex])]
        msg_chars = message_final
    message_final = caesar_decoded(message_final)

print("".join(map(str, message_final)))
