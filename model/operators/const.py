# Put in const.py...:
class _const:
    class ConstError(TypeError): pass
    def __setattr__(self,name,value):
        if name in  self.__dict__ :
            raise "Can't rebind const(%s)"%name
        self.__dict__[name]=value
        
        
import sys
sys.modules[__name__]=_const()


if  __name__ == "__main__":
    # that's all -- now any client-code can
    #import constants
    # and bind an attribute ONCE:
    #_const.magic = 23
    
    #print(_const.magic)
    # but NOT re-bind it:
    #constants.magic = 88      # raises const.ConstError
    # you may also want to add the obvious __delattr__
    pass