def play(roundNr,ownPrevMoves,otherPrevMoves,totalRounds):
    """
    Initialise by colluding, opening the possibility of cooperation.
    If cooperation works, end the game by defecting.
    
    If cooperation does not work, start defecting back
    """
    COLLUDE = 1
    DEFECT = 0
       
    if roundNr == 0:
        return COLLUDE
    
    if totalRounds - roundNr == 1:
        return DEFECT
    
    elif otherPrevMoves[-1] == COLLUDE:
        return COLLUDE
    else:
        if roundNr > 1 and ownPrevMoves[-2] == COLLUDE:
            return DEFECT
        else:
            return COLLUDE
        
def name():
    return "Het laatste woord"