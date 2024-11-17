from tkinter import *

import sqlite3

from tkinter import messagebox

from tkinter import filedialog

from geopy.geocoders import Nominatim
from geopy import distance
import sys

def open26():
    class addLocation:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            #Establishes front end requirements
            self.title = Label(window, text="Add Locations", font = "Verdana 32 bold").pack(pady=5)
            startLabel = Label(window, text="Start Location",font = "Verdana 14 bold").pack(pady=5)
            start1 = StringVar(window)
            start2 = StringVar(window)
            start3 = StringVar(window)
            start4 = StringVar(window)
            start5 = StringVar(window)
            self.entryStart = Entry(window, textvariable=start1).pack(pady=5)
            labelMiddle = Label(window, text="Lcations within",font = "Verdana 14 bold").pack(pady=5)
            self.entryMiddle1 = Entry(window, textvariable=start2).pack(pady=5)
            self.entryMiddle2 = Entry(window, textvariable=start3).pack(pady=5)
            self.entryMiddle3 = Entry(window, textvariable=start4).pack(pady=5)
            endLabel = Label(window, text="End Location",font = "Verdana 14 bold").pack(pady=5)
            self.entryMiddle4 = Entry(window, textvariable=start5).pack(pady=5)
           

            #Function for identifying the latitude and longitude of locations entered by the user. 
            #Takes 3 lists as arguments. 
            #2 for storage and 1 for analysis.
            #Uses the geopy package to identfiy information.
            def findLatLong(lists, lat, long):
                x = 0
                for location in lists:
                    geoCoder = Nominatim(user_agent="My application")
                    distination = geoCoder.geocode(location)
                    #Try and except used to deal with locations which are invalid. 
                    try:
                        #Identifies the latitude and longitiude of a desintation, and appends the value into a list. 
                        lat.append(distination.latitude)
                        long.append(distination.longitude)
                    except AttributeError:
                        x+=1
                        messagebox.showinfo(message="Locations are invalid" + str(x))
                try:  
                    return lat, long
                except:
                    messagebox.showinfo(message="An error occured.")
            

            #Automatically creates a graph for Djikstra Algorithim 
            #Takes 5 locations as arguments
            #Connects the locations together
            #Adds the neccessary weights.
            #Embedded within the function is also Dijikstra Algorithim.
            try:
                def calculateRoute(location1, location2, location3, location4, location5):
                        geoCoder = Nominatim(user_agent="My application")
                        sourceDist = "East London"
                        sourceDistination = geoCoder.geocode(sourceDist)
                        sourcelat = sourceDistination.latitude
                        sourcelong = sourceDistination.longitude
                        place1 = (sourcelat, sourcelong)

                        locationStorage = [location1, location2, location3, location4, location5]
                        latStorage = []
                        longStorage = []
                        

                        def createGraph(lat, long):
                            graph = {
                                sourceDist:{location1:float(distance.distance(place1, (lat[0], long[0])).km),location2:float(distance.distance(place1, (lat[1], long[1])).km)},
                                location1:{sourceDist:float(distance.distance(place1, (lat[0], long[0])).km), location2:float(distance.distance((lat[0], long[0]), (lat[1], long[1])).km), location3:float(distance.distance((lat[0], long[0]), (lat[2], long[2])).km), location4:float(distance.distance((lat[3], long[3]), (lat[0], long[0])).km)},
                                location2:{sourceDist:float(distance.distance(place1, (lat[1], long[1])).km), location1:float(distance.distance((lat[0], long[0]), (lat[1], long[1])).km), location4:float(distance.distance((lat[3], long[3]), (lat[1], long[1])).km), location3:float(distance.distance((lat[2], long[2]), (lat[1], long[1])).km)},
                                location3:{location1:float(distance.distance((lat[0], long[0]), (lat[2], long[2])).km), location2:float(distance.distance((lat[1], long[1]), (lat[2], long[2])).km), location4:float(distance.distance((lat[3], long[3]), (lat[2], long[2])).km), location5:float(distance.distance((lat[4], long[4]), (lat[2], long[2])).km)},
                                location4:{location2:float(distance.distance((lat[1], long[1]), (lat[3], long[3])).km), location3:float(distance.distance((lat[2], long[2]), (lat[3], long[3])).km), location1:float(distance.distance((lat[0], long[0]), (lat[3], long[3])).km), location5:float(distance.distance((lat[4], long[4]), (lat[3], long[3])).km)},
                                location5:{location3:float(distance.distance((lat[2], long[2]), (lat[4], long[4])).km), location4:float(distance.distance((lat[3], long[3]), (lat[4], long[4])).km)}
                            }
                            print(graph)
                            return graph
                        COST = 0  
                        PREVIOUS = 1

                        def djikstra(graph, source):
                            visisted = {}
                            unvisted = {}
                            for node in graph:
                                unvisted[node]= [sys.maxsize, None]
                            unvisted[source][COST] = 0
                            finished = False
                    
                            while finished == False:
                                if len(unvisted) == 0:
                                    finished = True
                                else:
                                
                                    current_node = min(unvisted, key = unvisted.get)
                                    neig = graph[current_node] 
                                    for node in neig:
                                        if node not in visisted:
                                            cost = unvisted[current_node][COST] +  neig[node]
                                            print(cost, node)
                                    
                                            if cost < unvisted[node][COST]:
                                                unvisted[node][COST] = cost
                                                unvisted[node][PREVIOUS] = current_node
                                    visisted[current_node] = unvisted[current_node]

                                            
                                    del unvisted[current_node]
                            return visisted
                        def findPath(graph):
                            visited = {}
                            unvisted = {}
    
                            for node in graph:
                                inf = 9999999999999
                                unvisted[node] = inf
                            finished = False
                            
                  
                        def djikstra2(graph, source):
                            visisted = {}
                            unvisted = {}
                            for node in graph:
                                unvisted[node]= [sys.maxsize, None]
                            unvisted[source][COST] = 0
                            finished = False
                    
                            while finished == False:
                                if len(unvisted) == 0:
                                    finished = True
                                else:
                                
                                    current_node = max(unvisted, key = unvisted.get)
                                    neig = graph[current_node] 
                                    for node in neig:
                                        if node not in visisted:
                                            cost = unvisted[current_node][COST] +  neig[node]
                                            print(cost, node)
                                    
                                            if cost > unvisted[node][COST]:
                                                unvisted[node][COST] = cost
                                                unvisted[node][PREVIOUS] = current_node
                                    visisted[current_node] = unvisted[current_node]

                                            
                                    del unvisted[current_node]
                            return visisted
                        
                            

                        #Finding shorest path 
                        def display(visited, startNode):
                    
                            for node, neigh in visited.items():
                                if node != startNode:
                                    current_node = node
                                    path = node

                                    while current_node != startNode:
                                        previous_node = visited[current_node][PREVIOUS]
                                        path = previous_node +"-" +path 

                                        current_node = visited[current_node][PREVIOUS]
                                    print(path)
                            return path
                        def display2(visited, startNode):
                    
                            for node, neigh in visited.items():
                                if node != startNode:
                                    current_node = node
                                    path = node

                                    while current_node != startNode:
                                        try:
                                            previous_node = visited[current_node][PREVIOUS]
                                        
                                            path = previous_node +"-" +path 
                                    

                                            current_node = visited[current_node][PREVIOUS]
                                        except:
                                            print('non')
                                            break
                                    print(path)
                            return path

                        
                        findLatLong(locationStorage, latStorage,longStorage)
                

                    
                        label = Label(window, text=display(djikstra(createGraph(latStorage, longStorage), "East London"), "East London"),font = "Verdana 14 bold").pack(pady=5)
                        print("----")
                        label2 = Label(window, text=findPath(createGraph(latStorage, longStorage)),font = "Verdana 14 bold").pack(pady=5)
                        
                 

                        
            except:
                messagebox.showinfo(message="The locations are invalid")




            button1 = Button(window, text="Calculate Route", command=lambda:calculateRoute(start1.get(), start2.get(), start3.get(), start4.get(), start5.get()), font = "Verdana 14 bold").pack(pady=5)



          
           
            

    window = Tk()
    obj = addLocation(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()