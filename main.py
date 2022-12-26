# bitmap generator, takes a string and generates a bitmap of the string on an image
import sys

# this string can be changed to any image (ASCII art). Art courtesy of https://inventwithpython.com/bitmapworld.txt
bitmap = """
       ....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

# should create a few more bitmap variables and let the user choose from several

print('Enter a string to generate a bitmap image of the world.')
message = input('> ')
if message == '':
    sys.exit()

# loop over each line in the bitmap
for line in bitmap.splitlines():
    # loop over each character in the line
    for i, bit in enumerate(line):
        if bit == ' ':
            # print an empty space
            print(' ', end='')
        else:
            # print a character from the message, when message ends, restart message until filled
            print(message[i % len(message)], end='')
    print()  # print a new line
