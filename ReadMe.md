# Goofer

The Goofer is a funny malware that displays a popup and start playing loud goofy sounds !

If the victim tries to shut down the popup another one is openned with a cotation about sucess, the "AUUUUUUUUUGGHHHH" 
meme song starts playing and the PC's volume is turned up !

You can only close the program in the task manager

The program is only visible in the task manager and the goofy process is launched when users press the space key
4 to 12 times (random).

I created it to prank my teammates whenever they don't lock their PCs !

## Disclaimer

This litle programm is **harmless** for the computer and has only been created for fun purposes.

## Dependencies

pygame
tkinter
pyinstaller
random
PIL

## Create the .exe

In order to create the .exe file execute the following command

`$ pyInstaller --onefile goofer.pyw `

Then copy/paste the assets (musics and pic) to the dist folder that has been generated.

The executable is located on the dist file.

Copy/paste the whole thing inside a USB Key and start to goof your distracted teammates !
