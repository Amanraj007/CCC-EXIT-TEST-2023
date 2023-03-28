def cutThemAll(lengths, minLength):
    total_length = sum(lengths)
    if total_length < minLength:
        return "Impossible"
    
    current_length = 0
    for i in range(len(lengths)):
        if current_length + lengths[i] < minLength:
            current_length += lengths[i]
        else:
            current_length = max(current_length, lengths[i])
            if i == len(lengths) - 1 and current_length >= minLength:
                return "Possible"
            current_length -= minLength
    
    return "Impossible"
