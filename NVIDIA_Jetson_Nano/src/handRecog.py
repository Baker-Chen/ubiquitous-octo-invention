def handrecongnition(fingerlist):
    ''' recognition_list = ['1','2','3','4','5','6','7'
                            ,'8','9','ok','open','close']'''
    if(fingerlist == [0,1,0,0,0]):
        return '1'
        
    elif(fingerlist == [0,1,1,0,0]):
        return '2'
        
    elif(fingerlist == [0,1,1,1,0]):
        return '3'
        
    elif(fingerlist == [0,1,1,1,1]):
        return '4'
        
    elif(fingerlist == [1,1,1,1,1]):
        return '5'
        
    elif(fingerlist == [1,0,0,0,1]):
        return '6'
        
    elif(fingerlist == [1,1,0,0,0]):
        return '7'
        
    elif(fingerlist == [1,1,1,0,0]):
        return '8'
        
    elif(fingerlist == [1,1,1,1,0]):
        return '9'

    elif(fingerlist == [0,0,0,0,1]): # or fingerlist == [0,0,0,0,0]
        return 'close'

    elif(fingerlist == [0,1,0,0,1]):
        return 'open'
        
    elif(fingerlist == [0,0,1,1,1] or fingerlist == [1,0,1,1,1]):
        return 'ok'
        
    else:
        return 'x'