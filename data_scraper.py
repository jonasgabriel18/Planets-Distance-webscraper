import requests
import json

planets = ['mercury', 'venus', 'mars', 'jupiter', 'saturn', 
            'uranus', 'neptune', 'pluto']

for planet in planets:
    url = f"https://theskylive.com/objects/{planet}/chartdata_dg.json"
    response = requests.get(url).text #Get the json data file

    with open(f"./data/{planet}.txt", "w") as initial_file: #Write it into a .txt to evaluate how the content is displayed
        initial_file.write(response)

    distances = dict() #The dict that will contain the relevant points

    with open(f"./data/{planet}.txt", "r") as f:
        content = f.readlines()[10:-1] #Slice the first 10 lines and the last one, they do not contain relevant information

        janeiro = False #Assistant boolean variables to read only distances in january and july
        julho = False

        for lines in content:
            linha = lines.replace("[", '').replace("]", '').split(',') #Clean the line and split into datetime, magnitude and distance
            data = linha[0][4:-2] #Get only the datetime
            
            if int(data[0:4]) <= 2025: #read only 12 years of data twice a year
                if data[5:7] == "01" and not janeiro:
                    distances[data] = linha[2]
                    janeiro = True
                    julho = False
                elif data[5:7] == "07" and not julho:
                    distances[data] = linha[2]
                    julho = True
                    janeiro = False
            
    with open(f"./data/{planet}.json", "w") as output_file:
        json.dump(distances, output_file, indent=2)  #Save the dict as a json