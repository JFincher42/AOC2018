'''
Basic rectangle class
'''

class Rect:
    '''
    A Rect is defined by four points:
    - left and top corner coordinates
    - width and height

    The overlap function takes another Rect, and returns a new rectangle
    representing the overlap area, or 
    '''

    def __init__(self, l, t, w, h):
        self.left = l
        self.top  = t
        self.width = w
        self.height = h

    def overlap(self, other):
        left = max(self.left, other.left)
        right = min(self.left+self.width, other.left+other.width)

        top = max(self.top, other.top)
        bottom = min(self.top+self.height, other.top+other.height)

        if (right-left)>0 and (bottom-top)>0:
            return Rect(left, top, right-left, bottom-top)
        else:
            return None
