from flask import Flask, render_template, request
import json

def create_app():
    app = Flask(__name__)



    @app.route("/")
    def home():
        return render_template("home.html")
    
    @app.route("/submit-page", methods=['POST'])
    def submit_info():
        
        user = request.form.get('username', '')
        info = request.form.get('information', '')

        
        with open('app/static/json/jsonfile.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(request.form, indent=4))
            
            
        return render_template("submit.html", user=user, info=info)
    
        
    
    return app

