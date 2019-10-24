while True:
    def buggy(arg, result=None):
        if result is None:
            result=[]
        result.append(arg)
        print (result)
    buggy('a')
    buggy ('c')
   
        
     
        
