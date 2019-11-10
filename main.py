# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:02:32 2018

@author: Ariclenes Silva
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:21:56 2018

@author: Ariclenes Silva
"""
import requests
from flask import Flask, render_template, request, redirect, jsonify, url_for, session as session2

from back_end_spotify import spotify_back_end

app = Flask(__name__)   

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        p_a = request.form['post_albums']
        mc=str(p_a)
        album_name = mc.split()
        album_name_final=""
        for i in album_name:
        	album_name_final+=i
        	album_name_final+="+"
        
        album_name_final=album_name_final[:-1]
        
        sbe=spotify_back_end(album_name_final)
        final_result=sbe.start()
        return render_template('post_album2.html', final_result_spotify=final_result)
    else:
        return render_template('post_album.html')
    

@app.errorhandler(404)
def page_not_found(error):
    #return render_template('page_not_found.html'), 404
    return "page_not_found"

@app.errorhandler(500)
def page_overload(e):
    return str(e)

with app.test_request_context():
    print(url_for('home'))


    
if __name__ == '__main__':
    app.debug = True
    app.run()