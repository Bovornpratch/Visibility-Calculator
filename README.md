# Visibility-Calculator


These scripts calculate the visibility of celestial objects and the moon. It is designed to be used as a backend function module which can be imported into othere scripts if nessesary. 

The script utilizes the following python modules.
    numpy
    matplotlib
    ephem >> special thanks to the pyephem team
These modules can be installed via 
    
    pip install numpy matplotlib ephem
    
the ephem module also utilizes python-tk which can be install with apt-get

    sudo apt-get install python-tk

The scipt input includes
	
	The observation date: YYYY-MM-DD format
	The observer time: Hr:Min:sec
    The object right ascention: Hr:Min:Sec
    The object declination: Deg:Min:Sec
	The observing latitude: Deg:Min:Sec format
	The observing longitude: Deg:Min:Sec format
	The observing elevation: int/float number
	
    Example Input:
    
    	python VisObject2.py 2017-06-23 00:00:00 18:36:56.48 +38:47:07.3 18:47:25.08 98:58:54.11 0

The script's output includes the time and date, the object's altitude, and the moon's altitude. However, truth is that the script also calculates the azimuthal angle of both objects too but it has been left out of the print out. 

	example output:
	
		2016/06/23 22:22:22  23.3413 -1.234234


