# Visibility-Calculator


These scripts calculate the visibility of celestial objects and the moon. It is designed to be used as a backend function module which can be imported into othere scripts if nessesary.

The script utilizes the following python modules.
    numpy
    matplotlib
    ephem
These modules can be installed via 
    
    pip install numpy matplotlib ephem
    
the ephem module also utilizes python-tk which can be install with apt-get

    sudo apt-get install python-tk

the scirpt takes in the right ascention(RA), Declination(DEC), Latittude(LAT), longitude(LONG) and the elevation(Elev) in sexidecimal form (Hr:min:secs , deg:':"). However, ELEV takes in normal numbers.

    python VisObject.py RA(hr:min:sec) DEC(deg:':") LAT(deg:':") LONG(deg:':") ELEV 
    python VisMoon.py LAT(deg:':") LONG(deg:':") ELEV 

Currenty it is set to print out the numbers on screen in to column forms including TIME/DATE and Altitude. However one may use the 'Printer' function to export the calculation to an ASCII text file.

