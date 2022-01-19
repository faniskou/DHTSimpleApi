# DHTSimpleApi
A simple python Api for DHT humidy temp sensors using Adafruit_DHT  
Should work with DHT11 , DHT22 , AM2302  
Have been tested on rasberry pi w , pi 4 with AM2302

## Use
you must offcourse have already installed python3 and pip3  
  
### first you must install the above python packages  
pip3 install Adafruit_Python_DHT  
pip3 install Flask  
pip3 install Flask-RESTful  
  
### hardcode the below values 
Choose your GPIOx port  
Choose your sensor Adafruit_DHT.AM2302 , Adafruit_DHT.DHT11 , Adafruit_DHT.DHT22  
  
### run the app  
No port is assigned so will propably run on 5000  
you can run the api by running python3 dht.py  

### run on rasbian as a service  
Use the above commands to install  
sudo cp dht.service /lib/systemd/system/  
sudo chmod 644 /lib/systemd/system/dht.service  
sudo systemctl daemon-reload  
sudo systemctl enable dht.service  
sudo systemctl start dht.service  
sudo systemctl status dht.service 
