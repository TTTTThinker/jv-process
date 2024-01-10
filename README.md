# JV Process
**A simple program for jv data processing.**
  
To run this program with command line, you can :  
> python jv.py *\$data_source_directory* *\$output_filename*  

To run this program with graphic window, you can :  
> python jv-ui.py  

To build an executable binary, you can :
  1. Install *pyinstaller* :
      > pip install pyinstaller
  2. Build executable binary :  
      > pyinstaller -w -F jv-ui.py
  3. Find the binary **jv-ui.exe** in the directory *dist/* .