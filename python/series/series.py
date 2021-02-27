def slices(series: str, length: int):
    if (not series) or (length<=0) or (length>len(series)):
        raise ValueError('Parameters not valid')
    return [series[i:i+length] for i in range(0,len(series)-length+1)]