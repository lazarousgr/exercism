def convert(number):
    raindrop_sound = ""
    
    if number % 3 == 0:
        raindrop_sound = "Pling"        
    if number % 5 == 0 :
        raindrop_sound += "Plang"
    if number % 7 == 0:
        raindrop_sound += "Plong"
        
    if len(raindrop_sound) == 0:
        raindrop_sound = str(number)

    return raindrop_sound