
from scipy.spatial import distance
import math

def euclidean(p1, p2):
    return distance.euclidean(p1, p2)

def distanceHaversine(p1, p2):
    p2 = np.squeeze(np.asarray(p2)) # Transform matrix 1,2 into an array with coord
    
    lat1 = p1[1]
    lng1 = p1[0]
    lat2 = p2[1]
    lng2 = p2[0]
   
    earthRadius = 3959
   
    lat1Rad = lat1 * math.pi/180
    lat2Rad = lat2 * math.pi/180
   
    Dlat = (lat2 - lat1) * math.pi/180
    Dlng = (lng2 - lng1) * math.pi/180
   
    a = pow(math.sin(Dlat/2), 2) + math.cos(lat1Rad) * math.cos(lat2Rad) * pow(math.sin(Dlng/2), 2)
   
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
   
    return (c * earthRadius)