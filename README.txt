cntdwnclk.py

Program name: Countdown Timer
Program Creator: promontorycoder
Program Language: python3

Purpose of Program: 
    Provide current time and countdown timer with alarm that sounds when zero
    time is reached.
    
    Creator used to help with python, tkinter and python modules learning.

Credits:
    Similar code found on multiple code learning websites. Code seen here is 
    author's own modification and adaptation of many. 

________________________________________________________________________________

REQUIREMENTS FOR UBUNTU 20.04
________________________________________________________________________________

#   If not already installed, install the following via terminal by
#   entering the commands below in the order they are given.
    
python3
    sudo apt-get install -y python3
    
tkinter
    sudo apt-get install -y python3-tk 
        
________________________________________________________________________________

GIT CLONE LINK
________________________________________________________________________________

# To git clone into the repository folder, enter the following command into 
# Terminal after navigating from within Terminal to the folder you'd like the
# program folder to be cloned to.

git clone https://github.com/promontorycoder/countdown_timer_tkinter.git  
________________________________________________________________________________

INSTALLATION INSTRUCTIONS FOR UBUNTU 20.04 FOR RUNNING FROM APPLICATIONS MENU
________________________________________________________________________________

Step 1: Collect all needed files
    Copy all files via git clone or other method into desired folder
    
Step 2: Make files executable
    Open gnome-terminal session and navigate to folder containing program files
    Make the .desktop, bash and python files executable by entering the
    following commands into the terminal and pressing [ENTER] after each command:
        chmod +x countdown_clock.desktop
        chmod +x cntdwnclk.sh
        chmod +x cntdwnclk.py
        
Step 3: Modify .desktop file and place in correct location
    Open the .desktop file with the following command:
        sudo gedit countdown_clock.desktop
        modify the file path in lines 5, 6 and 7 to reflect your file structure
        Save and close gedit
    Type the following command into gnome-terminal, changing path to and file to
    reflect your computer's file structure
        cp /path/to/file/countdown_clock.desktop /usr/share/applications/
        
Step 4: Program is installed
    Exit gnome-terminal and open applications menu.
    The program is named "Countdown Timer"
    
Note: If you do not have gedit installed already ...
    sudo apt-get install -y gedit
    
