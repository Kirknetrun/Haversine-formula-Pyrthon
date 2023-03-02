# Haversine-formula-Python
Haversine formula coded in Python function based on:

a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)

c = 2 ⋅ atan2( √a, √(1−a) )

d = R ⋅ c

where φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km)

angles need to be in radians to pass to trig functions

Source: https://www.movable-type.co.uk/scripts/latlong.html

Shown function is taking coordinates from four colums in dataframe to calculate them later. 

For instance you can use it on some dataframe using .apply() and lambda function:

     some_data_frame.apply(lambda x:haversine(x), axis=1)

