vooc = [5,6,11,0,9,8,10,15,1,2]

def search(vooc):
    idx = 0
    for element in vooc:
        if element == 10:
            print("Index Position: ", idx)
            
        idx+=1
        
print(search(vooc))