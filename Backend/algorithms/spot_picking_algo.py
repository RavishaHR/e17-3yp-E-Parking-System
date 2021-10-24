import json, sys
from dataclasses import dataclass

@dataclass
class SpotNode:
    spotNo: str                 #Spot Number
    distances: 'dict[str: int]'         #Dictionary of distances



if __name__ == "__main__":

    try:
        last_assigned_spot = sys.argv[1] #Get last assigned spot from database

        #ParkingSpots = json.loads('''[{"_id": "6149d25148c0381f44efecdc", "spotno": "A001", "state": "Occupied", "floornumber": 1, "__v": 0 }, {"_id": "616d64f59e349513982c71bd", "spotno": "A002", "state": "Not Occupied", "floornumber": 1, "__v": 0 }, {"_id": "616d65279e349513982c71bf", "spotno": "A003", "state": "Not Occupied", "floornumber": 1, "__v": 0 }, {"_id": "616d652c9e349513982c71c1", "spotno": "A004", "state": "Not Occupied", "floornumber": 1, "__v": 0 }, {"_id": "616d65319e349513982c71c3", "spotno": "A005", "state": "Not Occupied", "floornumber": 1, "__v": 0 }, {"_id": "616d65369e349513982c71c5", "spotno": "A006", "state": "Not Occupied", "floornumber": 1, "__v": 0 }, {"_id": "616d653b9e349513982c71c7", "spotno": "A007", "state": "Not Occupied", "floornumber": 1, "__v": 0 }, {"_id": "616d65419e349513982c71c9", "spotno": "A008", "state": "Not Occupied", "floornumber": 1, "__v": 0 }, {"_id": "616d65459e349513982c71cb", "spotno": "A009", "state": "Not Occupied", "floornumber": 1, "__v": 0 }, {"_id": "616d654d9e349513982c71cd", "spotno": "A010", "state": "Not Occupied", "floornumber": 1, "__v": 0 }, {"_id": "617439c06d6b5504bea13023", "spotno": "B001", "state": "Not Occupied", "floornumber": 2, "__v": 0 }, {"_id": "617439d76d6b5504bea13025", "spotno": "B002", "state": "Not Occupied", "floornumber": 2, "__v": 0 }, {"_id": "617439eb6d6b5504bea13027", "spotno": "B003", "state": "Not Occupied", "floornumber": 2, "__v": 0 }, {"_id": "617439f46d6b5504bea13029", "spotno": "B004", "state": "Not Occupied", "floornumber": 2, "__v": 0 }, {"_id": "61743a006d6b5504bea1302b", "spotno": "B005", "state": "Not Occupied", "floornumber": 2, "__v": 0 }, {"_id": "61743a0a6d6b5504bea1302d", "spotno": "B006", "state": "Not Occupied", "floornumber": 2, "__v": 0 }, {"_id": "61743a146d6b5504bea1302f", "spotno": "B007", "state": "Not Occupied", "floornumber": 2, "__v": 0 }, {"_id": "61743a286d6b5504bea13031", "spotno": "B008", "state": "Not Occupied", "floornumber": 2, "__v": 0 }, {"_id": "61743a326d6b5504bea13033", "spotno": "B009", "state": "Not Occupied", "floornumber": 2, "__v": 0 }, {"_id": "61743a406d6b5504bea13035", "spotno": "B010", "state": "Not Occupied", "floornumber": 2, "__v": 0 }, {"_id": "61743a516d6b5504bea13037", "spotno": "C001", "state": "Not Occupied", "floornumber": 3, "__v": 0 }, {"_id": "61743a5c6d6b5504bea13039", "spotno": "C002", "state": "Not Occupied", "floornumber": 3, "__v": 0 }, {"_id": "61743a686d6b5504bea1303b", "spotno": "C003", "state": "Not Occupied", "floornumber": 3, "__v": 0 }, {"_id": "61743a716d6b5504bea1303d", "spotno": "C004", "state": "Not Occupied", "floornumber": 3, "__v": 0 }, {"_id": "61743a7a6d6b5504bea1303f", "spotno": "C005", "state": "Not Occupied", "floornumber": 3, "__v": 0 }, {"_id": "61743a846d6b5504bea13041", "spotno": "C006", "state": "Not Occupied", "floornumber": 3, "__v": 0 }, {"_id": "61743a8f6d6b5504bea13043", "spotno": "C007", "state": "Not Occupied", "floornumber": 3, "__v": 0 }, {"_id": "61743a996d6b5504bea13045", "spotno": "C008", "state": "Not Occupied", "floornumber": 3, "__v": 0 } ]''')

        ParkingSpots = json.loads(sys.argv[2])   #Get parking spot list

        #Car park is empty
        if last_assigned_spot == "Nothing":
            print("A001")
        else:
            #Initialize the graph
            with open("algorithms/spots.json") as spotsFile:
                
                json_obj = json.load(spotsFile)

                Spots = [SpotNode(**json_obj[i]) for i in range(len(json_obj))]

                for spot in Spots:
                    if(spot.spotNo == last_assigned_spot):
                        last_assigned = Spots.index(spot) #Get spot index corresponding to the spot from the json file

                #Finds available spots
                available = dict((k,v) for k,v in Spots[last_assigned].distances.items() if ParkingSpots[int(k)-1]["state"]=="Not Occupied")

                try:
                    nextSpotNode = Spots[int(max(available, key = lambda x: available[x]))-1]
                    print(nextSpotNode.spotNo, end="")
                except ValueError:
                    print("Car Park is full")
    except Exception as e:
        print(e)
