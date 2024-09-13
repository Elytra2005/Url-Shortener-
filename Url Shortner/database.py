from flask import request, g
import json

def handle():
    if request.method == "POST": # if request method used was post (data enterd)
        # gets data from the submitted form
        g.url_handle = request.form.get("furl")

        jsonData = {
            'Url': g.url_handle,
        }

        try:
            
            with open('storedurls.json', "r") as json_file:
                    Data = json.load(json_file)
                    
                
        except json.JSONDecodeError:
                Data = {}
        
        key = f"url_{len(Data) + 1}"  # Generating a new unique key
        Data[key] = jsonData #assigning value key fron Data to JsonData


        with open('storedurls.json', 'w') as json_file:
            json.dump(Data, json_file)


        print(Data)

    else:
        print("idk bruh what did you do")


