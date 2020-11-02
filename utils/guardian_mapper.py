import constant, sys

def spacer():
    return "*****************"

def calculate_spawn_location (start_x_coordinate, start_z_coordinate):
    coordinate_map = []
    for x_coordinate in constant.GUARDIAN_SPAWN_MAP:
        for z_coordinate in constant.GUARDIAN_SPAWN_MAP:
            coordinate_map.append("{0},{1}".format(x_coordinate + start_x_coordinate, z_coordinate + start_z_coordinate))
    return coordinate_map

try:
    coords_map = calculate_spawn_location (int(sys.argv[1]), int(sys.argv[2]))
    coord_count = 1
    print (spacer())
    print ("*** Guardian Spawn Mapper 1.0 ***\n")
    print ("NorthWest Corner of Monument ({0}, {1}) \n".format(int(sys.argv[1]), int(sys.argv[2])))
    for coordinate in coords_map:
        print ("Guardian Spawn Point {0}: {1}".format(coord_count, coordinate))
        coord_count = coord_count + 1
    print (spacer())
except: 
    print("Whoops, something went wrong")
    print("Please be sure to include the X and Z coordinates (separated by a space)")
    print("Of the northwest corner of the ocean monument to correctly")
    print("Calculate where the guardian spawning locations are")
    print("\n**** Note: Bedrock Only ****")
