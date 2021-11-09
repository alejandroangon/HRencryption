import math

def encryption(_str):
    _str = _str.replace(" ","")
    _str_len = len(_str)
    _sRootStr = math.sqrt(_str_len)
    _rows = math.floor(_sRootStr)
    _cols = math.ceil(_sRootStr)
    _cont = 0
    _grid = []
    _strings = []
    _string = ""

    for i,x in enumerate(range(_rows)):
        _grid.append([])
        for j,y in enumerate(range(_cols)):
            if (_cont >= _str_len):
                _grid[i].append(None)
                continue
            _grid[i].append(_str[_cont])
            _cont+=1

    for a in range (_cols):
        _strings.append("")

    for i,x in enumerate(_grid):
        for j,y in enumerate(x):
            if (y==None):
                continue
            _strings[j]+= str(x[j])


    for x in _strings:
        _string += x + " "
    
    _string = _string[0:len(_string)]
    print(_string)
    return _string
