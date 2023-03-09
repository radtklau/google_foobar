#how this solution works: basecally I figuered out the formulas with which you can calulate an outer gear gear_radius, based on 
#an inner gear gear_radius (one formula for the left outer gear, on for the right outer gear), than i just set them equal like that:
#formula1=2*formula2 (2* because the left outer gear has to be double the size of the right outer gear) and solve for the variable.
#for even numbers I additionally have the formula x+y = right_middel_gear_gear_radius-left_middle_gear_gear_radius, where x and y are the gear_radius
#of the left middle gear and the right middle gear

def solution(pegs):

    if len(pegs) == 2: #seperate handling if len(pegs) is only 2
        num = pegs[1]-pegs[0]
        num *= 2
        g_c_d = gcd(num,3)

        num = num/g_c_d
        denom = 3 
        denom = denom / g_c_d
        gear_radius = [num,denom]
        return gear_radius
        
    #odd amount of pegs
    elif(len(pegs) % 2 != 0):
        start_index = int(len(pegs)/2) #start in the middle
        for peg in range(start_index): #build and shorten formula
            dist_left = pegs[start_index-peg]-pegs[start_index-(peg+1)] #shorten left formula
            dist_right = pegs[start_index+peg+1]-pegs[start_index+peg] #shorten right formula
            if peg >= 1: #subtract values from loop before
                dist_left -= dl
                dist_right -= dr
            dl = dist_left #remember values for next loop
            dr = dist_right

        left_x_coeff = (-1)**(start_index) #calculate variable sign
        right_x_coeff = ((-1)**(start_index))*2

        dist_right *= 2 #right side of equation times 2, because the outer left gear has to have double the gear_radius of the outer right gear

        #solve equation for x
        if dist_left < 0:
            right_side = dist_right+(-1*dist_left)
        else:
            right_side = dist_right-dist_left

        if right_x_coeff < 0:
            left_side = left_x_coeff + (-1*right_x_coeff)
        else:
            left_side = left_x_coeff - right_x_coeff

        x = right_side/left_side 
        if x < 1:
            return [-1,-1]

        #check for collision with pegs when needed gear sizes are applied
        gear_rad = x
        for peg in range(start_index): #from the middle to the right
            if pegs[start_index+peg] + gear_rad <= pegs[start_index+peg+1] - 1: #enough room
                gear_rad = (pegs[start_index+peg+1] - pegs[start_index+peg]) - gear_rad #calculate gear size for next loop
                continue
            else: #collision
                return [-1,-1]
        gear_rad = x
        for peg in range(start_index): #other direction
            if pegs[start_index-peg] - gear_rad >= pegs[start_index-peg-1] + 1:
                gear_rad = (pegs[start_index-peg] - gear_rad) - pegs[start_index-peg-1]
                continue
            else:
                return [-1,-1]

        g_c_d = gcd(right_side,left_side)
        nom = right_side/g_c_d
        denom = left_side/g_c_d
        dist_left *= denom
        if left_x_coeff < 0:
            nom = dist_left - nom
        else:
            nom = dist_left + nom

        g_c_d = gcd(nom,denom)
        nom = nom / g_c_d
        denom = denom / g_c_d

        if nom < 1 or denom < 1:
            return [-1,-1]
        gear_radius = [nom,denom]

    #even amount of pegs
    else:
        start_index = int((len(pegs)/2)-1) #start at the left middle peg
        dist_mid = pegs[start_index+1]-pegs[start_index] #distance between middle pegs
        for peg in range(start_index): #build and shorten formula
            dist_left = pegs[start_index-peg]-pegs[start_index-(peg+1)] #to the left
            dist_right = pegs[start_index+peg+2]-pegs[start_index+peg+1] #to the right

            if peg == 0: #in first loop subtract middle distance
                dist_left -= dist_mid  
            if peg != 0: #in all other loopx subtract previous value
                dist_left -= dl 
                dist_right -= dr
            dl = dist_left
            dr = dist_right
        left_y_coeff = (-1)**(start_index+1) #calc variable signs
        right_y_coeff = ((-1)**(start_index))*2

        dist_right *= 2 #right side of equation times 2

        #solve equation for y
        if right_y_coeff < 0:
            left_side = left_y_coeff + (-1*right_y_coeff)
        else:
            left_side = left_y_coeff - right_y_coeff
        
        if dist_left < 0:
            right_side = dist_right + (-1*dist_left)
        else:
            #print(dist_right)
            #print(dist_left)
            right_side = dist_right - dist_left

        y = float(right_side)/float(left_side)

        #print(y)
        if y < 1:
            return[-1,-1]

        #check for collisions with pegs for certain y
        gear_rad = y
        for i in range(start_index): #enough space
            if pegs[start_index+i+1] + gear_rad <= pegs[start_index+i+2] - 1:
                gear_rad = pegs[start_index+i+2] - (pegs[start_index+i+1] + gear_rad)
                continue
            else: #collision

                return [-1,-1]
        gear_rad = y
        for i in range(start_index+1):
            if pegs[start_index-i+1] - gear_rad >= pegs[start_index-i] + 1:
                gear_rad = (pegs[start_index-i+1] - pegs[start_index-i]) - gear_rad 
                continue
            else:
                return [-1,-1]

        g_c_d = gcd(right_side,left_side)
        nom = right_side/g_c_d
        denom = left_side/g_c_d
        dist_left *= denom
        if left_y_coeff < 0:
            nom = dist_left-nom
        else:
            nom = dist_left + nom
        
        g_c_d = gcd(nom,denom)
        nom = nom / g_c_d
        denom = denom / g_c_d
        if nom < 1 or denom < 1:
            return [-1,-1]

        gear_radius = [nom,denom]

    return gear_radius

def gcd(x, y): #greatest common denominator for fractions in simplest form
    while y != 0:
        (x, y) = (y, x % y)
    return x



