# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 22:59:04 2018

@author: Ariclenes Silva
"""
import urllib
#import urllib2
import json
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

location_on_map=[]
sim=True
class webServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        sim=True
        #href="/"
        try:
            if str(self.path)=="/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output+="""
                <!DOCTYPE html>
                <html>
                <head>
                <script>
                function myFunction() {
                   window.open('https://api.instagram.com/oauth/authorize/?client_id=6cdbb21972374382813c665d18401c72&redirect_uri=http://localhost:8094/&response_type=code','_self');
                }
                </script>
                </head>
                
                <body onload="myFunction()">
                <h1>Hello World!</h1>
                </body>
                
                </html>
                """
                
                self.wfile.write(output.encode(encoding='utf_8'))
                return
                
            if str(self.path)!="/home":
                self.payload = {
                    'client_id':'6cdbb21972374382813c665d18401c72',
                    'client_secret':'3f199abaa7804adcbf169fbafd13d851',
                    'grant_type':'authorization_code',
                    'redirect_uri':'http://localhost:8094/',
                    'code':'b2bef78b1b674260abd2f616fa6a53ce'
                }
                 
                self.send_response(200)
                self.end_headers() 
          #      self.send_header('Location','http://localhost:8094/home')
                self.send_header('Location','https://api.instagram.com/oauth/authorize/?client_id=6cdbb21972374382813c665d18401c72&redirect_uri=http://localhost:8094/&response_type=code')
                path=self.path
                path=path.split("code=")
                
                self.payload['code']=path[-1]
                
                if sim:
                    response = requests.post('https://api.instagram.com/oauth/access_token', data =self.payload,allow_redirects=False)
                    res=json.loads(response.content)
                    
                    response = requests.get('https://api.instagram.com/v1/users/self/media/recent/?access_token='+res['access_token'], allow_redirects=False)
                    res=json.loads(response.content)
                    
                    for i in res['data']:
                        location_on_map.append(i['location'])
                    
                sim=False
                
    #            self.send_header('Location','https://www.google.com')
                for i in location_on_map:
                    print(i)
            
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
             #   self.send_header('Location','http://localhost:8093/home')
                output = ""
                output+="""
                <!doctype html>
                <html>
                <head>
                <meta charset="utf-8">
                <title>Untitled Document</title>
                	
                	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                </head>
                
                <body>
                bjhnjknjnjknjknkj
                	<div><a class="btn btn-primary" href="/" style="top: 5%;left: 2%;position: absolute">Go back to HOMEPAGE</a></div>
                	<div style="top: 5%;left: 42%;position: absolute">Insert your informations to delete your account</div>
                	<div  style="top: 15%;left: 30%;position: absolute"> Please, your password should have at least one character and one number</div>
                	
                	<form method='POST' enctype='multipart/form-data' style="top: 35%;width: 70%;left: 10%;position: absolute">
                	  <div class="form-group">
                		<label for="exampleInputEmail1">Username</label>
                		<input type="text" name="delete_users_username" class="form-control" placeholder="Enter email or username">
                		<small id="emailHelp" class="form-text text-muted">We'll never share your username/email with anyone else.</small>
                	  </div>
                	  <div class="form-group">
                		<label for="exampleInputPassword1">Password</label>
                		<input type="password" name="delete_users_password" class="form-control" placeholder="Password">
                	  </div>
                      <input class="btn btn-primary" type="submit" value="Submit">
                	</form>
                	
                	<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                </body>
                </html>
                """
                
                self.wfile.write(output.encode(encoding='utf_8'))
                return
            
            else:
                print("nsfkjsdfjdsnfkjdsfdjbgjdfbhjnvjndjnkdfngjkdfngjkfdngkjdfngkjfdngkjdfngkjdf")
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output+="""
                <!doctype html>
                <html>
                <head>
                <meta charset="utf-8">
                <title>Untitled Document</title>
                	
                	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                </head>
                
                <body>
                	<div><a class="btn btn-primary" href="/" style="top: 5%;left: 2%;position: absolute">Go back to HOMEPAGE</a></div>
                	<div style="top: 5%;left: 42%;position: absolute">Insert your informations to delete your account</div>
                	<div  style="top: 15%;left: 30%;position: absolute"> Please, your password should have at least one character and one number</div>
                	
                	<form method='POST' enctype='multipart/form-data' style="top: 35%;width: 70%;left: 10%;position: absolute">
                	  <div class="form-group">
                		<label for="exampleInputEmail1">Username</label>
                		<input type="text" name="delete_users_username" class="form-control" placeholder="Enter email or username">
                		<small id="emailHelp" class="form-text text-muted">We'll never share your username/email with anyone else.</small>
                	  </div>
                	  <div class="form-group">
                		<label for="exampleInputPassword1">Password</label>
                		<input type="password" name="delete_users_password" class="form-control" placeholder="Password">
                	  </div>
                      <input class="btn btn-primary" type="submit" value="Submit">
                	</form>
                	
                	<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                </body>
                </html>
                """
                self.wfile.write(output.encode(encoding='utf_8'))
                return
        except:
            print("Error")

def main():
    try:
        port = 8094
        server = HTTPServer(('', port), webServerHandler)
        print ("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()

