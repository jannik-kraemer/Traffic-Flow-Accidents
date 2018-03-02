def rad(startPoint, destination):
    # diff_lat = startPoint['lat'] - destination['lat']
    lat = []
    lng = []
    lat.append(float(startPoint['lat']))
    lat.append(float(destination['lat']))
    lng.append(float(startPoint['lng']))
    lng.append(float(destination['lng']))

    centerlat = sum(lat)/len(lat)
    centerlng = sum(lng)/len(lng)

    print("Center lat: " + str(centerlat))
    print("Center lng: " + str(centerlng))
    return (centerlat, centerlng)