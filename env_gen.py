import numpy as np
import math, time, random


#neuron = [xyz],[n?], [n_id, n, nt1, kDown, kUp, linkedSynapses]
#plasma = [type, p, p+1, s_effect, p_supressor]

#synapse = [id],[e],[rIn],[rOut],[noE]


#x[y[z[],],],

def get_reference_matrix():
    reference = [[0,0,0],[0],[0,0,0,0,[0]],[0,0,0,0,0]]
    return reference

def get_reference_synapse():
    reference = [0,0,0,0,0]
    return reference

def create_synapses_array():
    reference = get_reference_synapse()
    synapsesArray = np.array(reference, dtype='f')
    return synapsesArray
 
def matrix_create_z(length):
    reference = get_reference_matrix()
    
    rows_array = [0]
    
    rows_array[0] = reference
              
    i = 1
    while (i<length):
        rows_array.append(reference)
        i=i+1
    
    return rows_array

def matrix_create_y(z_array, length):
    reference = z_array
    
    rows_array = [0]
    
    rows_array[0] = reference
    
    i = 1
    while (i<length):
        rows_array.append(reference)
        i=i+1
    
    return rows_array

def matrix_create_x(y_array, length):
    reference = y_array
    
    rows_array = [0]
    
    rows_array[0] = reference
    
    i = 1
    while (i<length):
        rows_array.append(reference)
        i=i+1
    
    return rows_array

def affect_coord_to_matrix(length, m):
    matrix = np.array(m)
    ix = 0
    while (ix<length):
        iy = 0
        while (iy<length):
            iz = 0
            while (iz<length):
                focus = matrix[ix,iy,iz]
                focus[0] = [ix,iy,iz]
                iz = iz+1                
            iy = iy+1
        ix = ix+1
    return matrix

def get_origin_coord(length):
    origin = (length-1)/2
    origin_coord = [origin, origin, origin]
    return origin_coord

def matrix_create(length):
    
    start_time = time.time()
    
    
    l = length
    
    z = matrix_create_z(l)
    yz = matrix_create_y(z,l)
    xyz = matrix_create_x(yz,l)
    
    matrix = affect_coord_to_matrix(l, xyz)
    
    origin_coord = get_origin_coord(l)
    
    end_time = time.time() - start_time 
    
    print end_time, "s to generate matrix"
    
    return matrix, origin_coord

def build_brain_environment(length, fileIndex):
    matrix, _, = matrix_create(length)
    synapsesArray = create_synapses_array()
    
    matrix_file_name = "matrix-" + str(fileIndex)
    syn_file_name = "synapses-" + str(fileIndex)
    
    np.save(matrix_file_name, matrix)
    print "File", matrix_file_name,".py saved"
    np.save(syn_file_name, synapsesArray)
    print "File", syn_file_name,".py saved"
    
    
def show_random_entries(k,m):
    m_length = len(m)-1
    
    i=0
    while(i<=k):
        x = random.randrange(0,m_length)
        y = random.randrange(0,m_length)
        z = random.randrange(0,m_length)
        
        print "Randomly choosen entries (",x,",",y,",",z,") n#",i,":",m[x,y,z]
        
        i = i+1
        
        

def distance(alpha,beta):

    a = alpha
    b = beta
    
    ax = a[0]
    ay = a[1]
    az = a[2]
    
    bx = b[0]
    by = b[1]
    bz = b[2]
    
    dx = abs(ax-bx)
    dy = abs(ay-by)
    dz = abs(az-bz)
    
    sqr_distance = (dx**2)+(dy**2)+(dz**2)
    distance = math.sqrt(sqr_distance)
    
    return distance
    
###########################"""

#build_brain_environment(50,"1820")   




#a = [2,3,4]
#b = [2,4,5]

#dis = distance(a,b)
#print "dist:", dis


    