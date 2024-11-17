from tkinter import *

import sqlite3
import sys

from tkinter import messagebox

from tkinter import filedialog




from geopy.geocoders import Nominatim
from geopy import distance




from addLocation import open26
def open16():
    class location:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            self.title = Label(window, text="Location Finder", font = "Verdana 32 bold").pack(pady=20)

            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()
            
            def openAddLocation():
                open26()
            button = Button(window, text="Add locations", command=openAddLocation).pack(pady=5)
            def insertIntoFormat(list1, result):
                for i in result:
                    list1.append(i[0])
                return list1
            #SQL statement used to select deliveryID from delivery 
            cursor.execute("SELECT DeliveryID FROM Delivery")
            queryResult = cursor.fetchall()
            queryResultStorage = []
            insertIntoFormat(queryResultStorage, queryResult)
            

            dropDown = StringVar(window)
            dropDown.set(queryResultStorage[0])
            drop1 = OptionMenu(window, dropDown, *queryResultStorage)
            drop1.pack(pady=20)
            drop1.configure(width=20)
            def get(deliveryID):
                #flag values
                x = 0
                y = 0
                z = 0
                m = 0
                #Connects to dataabase
                with sqlite3.connect("SalesOrderProcessing.db") as db:
                    cursor=db.cursor()
                #Parameterized SQL select statement 

                query = """SELECT Delivery.OrderID, 
                (SELECT Order1.ClientID FROM Order1 WHERE OrderID = Delivery.OrderID)
                FROM Delivery WHERE DeliveryID = ?"""
                cursor.execute(query, (deliveryID, ))
                query_info = cursor.fetchall()

                print(query_info[0][1])

                #Parameterized SQL select statement 
         
                #Parameterized SQL select statement  
              
         
        
                sql3 = """SELECT postCode FROM Client WHERE ClientID = ?"""
                cursor.execute(sql3, (query_info[0][1],),)
                queryResult3 = cursor.fetchall()
                queryResultStorage3 = []
                for j in queryResult3:
                    queryResultStorage3.append(j[0])
                print(queryResultStorage3[0])
                details = []
                for j in queryResultStorage3[0]:
                    details.append(j)
                print(details)
                #Post code initals 
                ps1 = ["LU", "2121", "WD", "MK", "CB", "CV"]
                ps2 = ["SL4", "SL6", "SL5", "RG5", "RG1"]
                ps3 = ["CR0", "RH19", "RH10", "RH16", "BN"]
                #Combines together user input post code initals 
                value1 = details[0] + details[1]
                print(value1)
                #Checks which initials the postcode belongs to, and iniates neccessary flag alert
                if value1 in ps1:
                    x+=1
                    print("Yes ps1")
                if value1 in ps2:
                    y+=1
                    print("Yes ps2")
                if value1 in ps3:
                    z+=1
                    print("Yes ps3")
                
                if x == 1:
                    #Uses geopackage to create distances 
                    geoCoder = Nominatim(user_agent="My application")
                    location1 = "East London"
                    sourceDistination = geoCoder.geocode(location1, timeout=None)
                    lat = sourceDistination.latitude
                    long = sourceDistination.longitude
            

                    place1 = (lat,long)

                    locationDet = queryResultStorage3[0]

                    sourceDistination2 = geoCoder.geocode(locationDet, timeout=None)
                    latNew3 = sourceDistination2.latitude
                    longNew3 = sourceDistination2.longitude
        
                    #Creation of nodes
                    lists = ["Luton", "Milton Keynes", "Dunchurch", "Epping", "Coventry"]

                    
                        
                    latitude1 =[]
                    longitude1 = []
                    #Calculating the latitude and longitude of locations through traversing throuhg the nodes.
                    for j in lists:
                        coordinates = geoCoder.geocode(j, timeout=None)
                        latitude1.append(coordinates.latitude)
                        longitude1.append(coordinates.longitude)
    
                    #Creation of an undirected graph
                    graph = {
                        "East London": {"Luton":float(distance.distance(place1, (latitude1[0], longitude1[0])).km), "Milton Keynes":float(distance.distance(place1, (latitude1[1], longitude1[1])).km)},
                        "Luton":{"East London":float(distance.distance(place1, (latitude1[0], longitude1[0])).km),"Milton Keynes":float(distance.distance((latitude1[0], longitude1[0]),(latitude1[1], longitude1[1])).km), "Dunchurch":float(distance.distance((latitude1[0], longitude1[0]),(latitude1[2], longitude1[2])).km), queryResultStorage3[0]:float(distance.distance(place1,(latNew3, longNew3)).km)},
                        "Milton Keynes":{"East London":float(distance.distance(place1, (latitude1[1], longitude1[1])).km), "Luton":float(distance.distance((latitude1[0], longitude1[0]),(latitude1[1], longitude1[1])).km), "Epping":float(distance.distance((latitude1[1], longitude1[1]),(latitude1[3], longitude1[3])).km), queryResultStorage3[0]:float(distance.distance((latitude1[0], longitude1[0]),(latNew3, longNew3)).km)},
                        "Dunchurch":{"Luton":float(distance.distance((latitude1[0], longitude1[0]),(latitude1[2], longitude1[2])).km), "Epping":float(distance.distance((latitude1[2], longitude1[2]),(latitude1[3], longitude1[3])).km) ,"Coventry":float(distance.distance((latitude1[2], longitude1[2]),(latitude1[4], longitude1[4])).km), queryResultStorage3[0]:float(distance.distance((latitude1[1], longitude1[1]),(latNew3, longNew3)).km)},
                        "Epping":{"Milton Keynes":float(distance.distance((latitude1[1], longitude1[1]),(latitude1[3], longitude1[3])).km), "Dunchurch":float(distance.distance((latitude1[2], longitude1[2]),(latitude1[3], longitude1[3])).km), "Coventry":float(distance.distance((latitude1[3], longitude1[3]),(latitude1[4], longitude1[4])).km), queryResultStorage3[0]:float(distance.distance((latitude1[2], longitude1[2]),(latNew3, longNew3)).km)},
                        "Coventry":{"Dunchurch":float(distance.distance((latitude1[2], longitude1[2]),(latitude1[4], longitude1[4])).km), "Epping":float(distance.distance((latitude1[3], longitude1[3]),(latitude1[4], longitude1[4])).km), queryResultStorage3[0]:float(distance.distance((latitude1[4], longitude1[4]),(latNew3, longNew3)).km)},
                        queryResultStorage3[0]:{"Coventry":float(distance.distance((latitude1[4], longitude1[4]),(latNew3, longNew3)).km), "Epping":float(distance.distance((latitude1[3], longitude1[3]),(latNew3, longNew3)).km), "Dunchurch":float(distance.distance((latitude1[2], longitude1[2]),(latNew3, longNew3)).km),"Milton Keynes":float(distance.distance((latitude1[1], longitude1[1]),(latNew3, longNew3)).km),"Luton":float(distance.distance((latitude1[0], longitude1[0]),(latNew3, longNew3)).km), "East London":float(distance.distance(place1,(latNew3, longNew3)).km)}
                    }
                    display(djikstra(graph, "East London"), "East London")
                    label = Label(window, text=display(djikstra(graph, "East London"), "East London")).pack(pady=5)
                

                if y==1:
                    #Uses geopackage to create distances 
                    geoCoder = Nominatim(user_agent="My application")
                    location1 = "East London"
                    sourceDistination = geoCoder.geocode(location1, timeout=None)
                    lat = sourceDistination.latitude
                    long = sourceDistination.longitude

                    locationDet = queryResultStorage3[0]

                    sourceDistination2 = geoCoder.geocode(locationDet, timeout=None)
                    latNew = sourceDistination2.latitude
                    longNew = sourceDistination2.longitude

            
                    #Calculating the latitude and longitude of locations through traversing throuhg the nodes.
                    place1 = (lat,long)
                    list1 = ["Windsor", "Maidenhead", "Ascot", "Woodley", "Reading"]
                    latitude1 =[]
                    longitude1 = []
                    for j in list1:
                        coordinates = geoCoder.geocode(j, timeout=None)
                        latitude1.append(coordinates.latitude)
                        longitude1.append(coordinates.longitude)
                    

                    #Creation of an undirected graph
                    graph = {
                        "East London":{"Windsor":float(distance.distance(place1, (latitude1[0], longitude1[0])).km), queryResultStorage3[0]:float(distance.distance(place1, (latNew, longNew)).km)},
                        "Windsor":{"East London": float(distance.distance(place1, (latitude1[0], longitude1[0])).km), "Ascot":float(distance.distance((latitude1[0], longitude1[0]), (latitude1[2], longitude1[2])).km), "Maidenhead":float(distance.distance((latitude1[0], longitude1[0]), (latitude1[1], longitude1[1])).km), queryResultStorage3[0]:float(distance.distance((latitude1[0],longitude1[0]), (latNew, longNew)).km)},
                        "Maidenhead":{"Windsor":float(distance.distance((latitude1[0], longitude1[0]), (latitude1[1], longitude1[1])).km), "Ascot":float(distance.distance((latitude1[1], longitude1[1]), (latitude1[2], longitude1[2])).km), "Woodley":float(distance.distance((latitude1[3], longitude1[3]), (latitude1[2], longitude1[2])).km), queryResultStorage3[0]:float(distance.distance((latitude1[1],longitude1[1]), (latNew, longNew)).km)},
                        "Ascot":{"Windsor":float(distance.distance((latitude1[1], longitude1[1]), (latitude1[2], longitude1[2])).km), "Maidenhead":float(distance.distance((latitude1[1], longitude1[1]), (latitude1[2], longitude1[2])).km), "Woodley":float(distance.distance((latitude1[3], longitude1[3]), (latitude1[2], longitude1[2])).km), queryResultStorage3[0]:float(distance.distance((latitude1[2],longitude1[2]), (latNew, longNew)).km)},
                        "Woodley":{"Maidenhead":float(distance.distance((latitude1[1], longitude1[1]), (latitude1[3], longitude1[3])).km), "Ascot":float(distance.distance((latitude1[3], longitude1[3]), (latitude1[2], longitude1[2])).km), "Reading":float(distance.distance((latitude1[3], longitude1[3]), (latitude1[4], longitude1[4])).km), queryResultStorage3[0]:float(distance.distance((latitude1[3],longitude1[3]), (latNew, longNew)).km)},
                        "Reading":{"Woodley":float(distance.distance((latitude1[3], longitude1[3]), (latitude1[4], longitude1[4])).km), queryResultStorage3[0]:float(distance.distance((latitude1[4],longitude1[4]), (latNew, longNew)).km)},
                        queryResultStorage3[0]:{"Reading":float(distance.distance((latitude1[4], longitude1[4]), (latNew, longNew)).km), "Woodley":float(distance.distance((latitude1[3], longitude1[3]), (latNew, longNew)).km), "Ascot":float(distance.distance((latitude1[2], longitude1[2]), (latNew, longNew)).km), "Maidenhead":float(distance.distance((latitude1[1], longitude1[1]), (latNew, longNew)).km), "Windsor":float(distance.distance((latitude1[0], longitude1[0]), (latNew, longNew)).km),"East London":float(distance.distance(place1, (latNew, longNew)).km) }
                    }
                    
                    display(djikstra(graph, "East London"), "East London")
                    #Creates file, with all details. 
                    let = []
                    let.append(display(djikstra(graph, "East London"), "East London"))
                    print(let)
                    
                    geoCoder = Nominatim(user_agent="My application")
                    location = queryResultStorage3[0]
                    sourceDistination = geoCoder.geocode(location, timeout=None)
                    lat2 = sourceDistination.latitude
                    long2 = sourceDistination.longitude
                    '''
                    file = dropDown.get()+"delivery"+".txt"
                    f = open(file, "w")
                    body = f"""

                    Subject: Delivery Details for DeliveryID {dropDown.get()}\n
                    Client PostCode: {queryResultStorage3[0]}\n
                    The Desired Delivery Route is within this channel: {let[0]}\n
                    Approximated Distance: {distance.distance(place1, (lat2, long2)).km}\n
                    
                    

                    """


                    f.write(body)
                    f.close()
                    '''
                    label = Label(window, text="File Downloaded with details")
                    label.pack()
                    label = Label(window, text=display(djikstra(graph, "East London"), "East London")).pack(pady=5)
                
                    
                if z == 1:
                    #Uses geopackage to create distances 
                    geoCoder = Nominatim(user_agent="My application")
                    location1 = "East London"
                    sourceDistination = geoCoder.geocode(location1, timeout=None)
                    lat = sourceDistination.latitude
                    long = sourceDistination.longitude
                    place1 = (lat,long)

                    locationDet = str(queryResultStorage3[0])
                    print(locationDet)

                    sourceDistination2 = geoCoder.geocode(locationDet, timeout=None)
                    latNew1 = sourceDistination2.latitude
                    longNew1 = sourceDistination2.longitude
                    #Calculating the latitude and longitude of locations through traversing throuhg the nodes.
                    list1 = ["Croydon", "Crawley", "East Grinstead", "Haywards Heath", "Brighton"]
                    latitude1 =[]
                    longitude1 = []
                    for j in list1:
                        coordinates = geoCoder.geocode(j, timeout=None)
                        latitude1.append(coordinates.latitude)
                        longitude1.append(coordinates.longitude)
                    #Creation of an undirected graph
                    graph = {
                        "East London":{"Croydon":float(distance.distance(place1, (latitude1[0], longitude1[0])).km), queryResultStorage3[0]:float(distance.distance(place1, (latNew1, longNew1)).km)},
                        "Croydon":{"East London": float(distance.distance(place1, (latitude1[0], longitude1[0])).km), "Crawley":float(distance.distance((latitude1[0], longitude1[0]), (latitude1[2], longitude1[2])).km), "East Grinstead":float(distance.distance((latitude1[0], longitude1[0]), (latitude1[1], longitude1[1])).km)},
                        "East Grinstead":{"Croydon":float(distance.distance((latitude1[0], longitude1[0]), (latitude1[1], longitude1[1])).km), "Crawley":float(distance.distance((latitude1[1], longitude1[1]), (latitude1[2], longitude1[2])).km), "Haywards Heath":float(distance.distance((latitude1[3], longitude1[3]), (latitude1[2], longitude1[2])).km), queryResultStorage3[0]:float(distance.distance((latitude1[0], longitude1[0]), (latNew1, longNew1)).km)},
                        "Crawley":{"Croydon":float(distance.distance((latitude1[1], longitude1[1]), (latitude1[2], longitude1[2])).km), "East Grinstead":float(distance.distance((latitude1[1], longitude1[1]), (latitude1[2], longitude1[2])).km), "Haywards Heath":float(distance.distance((latitude1[3], longitude1[3]), (latitude1[2], longitude1[2])).km), queryResultStorage3[0]:float(distance.distance((latitude1[1], longitude1[1]), (latNew1, longNew1)).km)},
                        "Haywards Heath":{"East Grinstead":float(distance.distance((latitude1[1], longitude1[1]), (latitude1[3], longitude1[3])).km), "Crawley":float(distance.distance((latitude1[3], longitude1[3]), (latitude1[2], longitude1[2])).km), "Brighton":float(distance.distance((latitude1[3], longitude1[3]), (latitude1[4], longitude1[4])).km), queryResultStorage3[0]:float(distance.distance((latitude1[2], longitude1[2]), (latNew1, longNew1)).km)},
                        "Brighton":{"Haywards Heath":float(distance.distance((latitude1[3], longitude1[3]), (latitude1[4], longitude1[4])).km), queryResultStorage3[0]:float(distance.distance((latitude1[4], longitude1[4]), (latNew1, longNew1)).km), queryResultStorage3[0]:float(distance.distance((latitude1[3], longitude1[3]), (latNew1, longNew1)).km)},
                        queryResultStorage3[0]:{"Brighton":float(distance.distance((latitude1[4], longitude1[4]), (latNew1, longNew1)).km), "Haywards Heath":float(distance.distance((latitude1[3], longitude1[3]), (latNew1, longNew1)).km), "Crawley":float(distance.distance((latitude1[2], longitude1[2]), (latNew1, longNew1)).km), "East Grinstead":float(distance.distance((latitude1[1], longitude1[1]), (latNew1, longNew1)).km), "Croydon":float(distance.distance((latitude1[0], longitude1[0]), (latNew1, longNew1)).km), "East London":float(distance.distance(place1, (latNew1, longNew1)).km)}
                    }
                    label = Label(window, text=display(djikstra(graph, "East London"), "East London")).pack(pady=5)
               
                 
            button = Button(window, text="Enter", command=lambda:get(dropDown.get()), font = "Verdana 14 bold").pack(pady=5)
            COSTFORMOVEMENT = 0  
            PREVIOUSCOSTMOVEMENT = 1
            try:
                #Finding visited and unvisited nodes
                def djikstra(graph, source):
                    visisted = {}
                    unvisted = {}
                    inf = sys.maxsize

                    #Sets all nodes equal to infinity
                    #The source node is set to 0. 
                    for node in graph:
                        unvisted[node]= [inf, None]
                    unvisted[source][COSTFORMOVEMENT] = 0
                    finished = False
                    #A loop to start breadth first search 
                    while finished == False:
                        #Checks if all nodes have been visited , if yes the loop stops.
                        if len(unvisted) == 0:
                            finished = True
                        else:
                            #The minimum cost of is identified from the graph.
                            current_node = min(unvisted, key = unvisted.get)
                            neig = graph[current_node] 
                            #Optimizes cost of node 
                            for node in neig:
                                if node not in visisted:
                                    cost = unvisted[current_node][COSTFORMOVEMENT] +  neig[node]
                                    print(cost, node)
                                    #Compares cost in each of the connections within the graph.
                                    if cost < unvisted[node][COSTFORMOVEMENT]:
                                        unvisted[node][COSTFORMOVEMENT] = cost
                                        unvisted[node][PREVIOUSCOSTMOVEMENT] = current_node
                            #Equates the visited and univisited nodes together.
                            visisted[current_node] = unvisted[current_node]    

                            del unvisted[current_node]
                    return visisted
                
    
                #Finding shorest path 
                #Finding shorest path 
                def display(visited, startNode):
            
                    for node, neigh in visited.items():
                        if node != startNode:
                            current_node = node
                            path = node

                            while current_node != startNode:
                                previous_node = visited[current_node][PREVIOUSCOSTMOVEMENT]
                                path = previous_node +"-" +path 

                                current_node = visited[current_node][PREVIOUSCOSTMOVEMENT]
                            print(path)
                    return path
            except:
                messagebox.showinfo(message="Postcode is not existent. ")


         
            


        
    

    window = Tk()
    obj = location(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()