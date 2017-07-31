"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    
    pass



def check_a(x,y,blank,move_list,move_list2):
    """ helper function for custom score"""
    l=0
    l2=0
    x1=x
    y1=y
    for u,v in move_list:
            x1=x1+u
            y1=y1+v
            if (x1,y1) in blank:
                l=l+1
            else:
                break
   
    x2=x
    y2=y
    for u,v in move_list2:
        x2=x2+u
        y2=y2+v
        if (x2,y2) in blank:
            l2=l2+1
        else:
            break
    
    return l+l2


def custom_score(game,player):
    """For details about the heuristic see heuristic_analysis.pdf

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """    
    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    
    
    blank=game.get_blank_spaces()
    x,y = game.get_player_location(player)
    
    a=[(2,1),(-2,1),(1,-2),(1,2),(-2,-1),(2,-1),(-1,2)]
    b=[(1, 2), (1, -2), (-2, 1), (2, 1), (-1, -2), (-1, 2), (2, -1)]
    c=[(2,-1),(-2,-1),(1,2),(1,-2),(-2,1),(2,1),(-1,-2)]
    d=[(1, -2), (1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2), (2, 1)]
    a2=[(-2, -1), (2, -1), (-1, 2), (-1, -2), (2, 1), (-2, 1), (1, -2)]
    b2=[(-1, -2), (-1, 2), (2, -1), (-2, -1), (1, 2), (1, -2), (-2, 1)]
    c2=[(-2, 1), (2, 1), (-1, -2), (-1, 2), (2, -1), (-2, -1), (1, 2)]
    d2=[(-1, 2), (-1, -2), (2, 1), (-2, 1), (1, -2), (1, 2), (-2, -1)]
    e=[(2,-1),(-1,2),(-1,-2),(2,1),(-2,1),(1,-2),(1,2)]
    f=[(2,1),(-1,-2),(-1,2),(2,-1),(-2,-1),(1,2),(1,-2)]
    e2=[(-2, -1), (1, 2), (1, -2), (-2, 1), (2, 1), (-1, -2), (-1, 2)]
    f2=[(-2, 1), (1, -2), (1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2)]
    g=[(1,-2),(-2,1),(2,1),(-1,-2),(-1,2),(2,-1),(-2,-1)]
    h=[(-1,-2),(2,1),(-2,1),(1,-2),(1,2),(-2,-1),(2,-1)]
    g2=[(1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2), (2, 1), (-2, 1)]
    h2=[(-1, 2), (2, -1), (-2, -1), (1, 2), (1, -2), (-2, 1), (2, 1)]

    l_sum=0
    
    if (x+2<=6) and (y+2<=6):
        l=check_a(x,y,blank,a,b)
        l_sum=l_sum+l
        
    if ((x+2<=6) and (y-2>=0)):
        l=check_a(x,y,blank,c,d)
        l_sum=l_sum+l
        
    if ((x-2>=0) and (y-2>=0)):
        l=check_a(x,y,blank,a2,b2)
        l_sum=l_sum+l
        
    if ((x-2>=0) and (y+2<=6)):
        l=check_a(x,y,blank,c2,d2)
        l_sum=l_sum+l
        
    if ((x+2<=6)and((y+1<=6)and(y-1>=0))):
        l=check_a(x,y,blank,e,f)
        l_sum=l_sum+l
        
    if ((x-2>=0)and((y+1<=6)and(y-1>=0))):
        l=check_a(x,y,blank,e2,f2)
        l_sum=l_sum+l
        
    if ((y-2>=0)and((x+1<=6)and(x-1>=0))):
        l=check_a(x,y,blank,g,h)
        l_sum=l_sum+l
        
    if ((y+2<=6)and((x+1<=6)and(x-1>=0))):
        l=check_a(x,y,blank,g2,h2)
        l_sum=l_sum+l
                    
    return float(l_sum)

def custom_score_1(game,player):
    """For details about the heuristic see heuristic_analysis.pdf

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """    

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    return 0

def custom_score_2(game,player):
    """For details about the heuristic see heuristic_analysis.pdf

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    def going_on(game_state,l=0,m_max=0):
        legal_moves=game_state.get_legal_moves(player)
        if len(legal_moves)==0:
            if l>m_max:
                m_max=l
            return m_max
        for m in legal_moves:
           game_state._active_player=player
           m_max=going_on(game_state.forecast_move(m),l+1,m_max)
        return m_max
        
    if len(game.get_blank_spaces())<=15:
        game_state=game.copy()
        x,y =game_state.get_player_location(player)
        m_max=going_on(game_state)
        return float(m_max)
    
    return float(0)



def custom_score_3(game,player):
    """For details about the heuristic see heuristic_analysis.pdf

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    def going_on(game_state,l=0,m_max=0):

        legal_moves=game_state.get_legal_moves(player)
     
        if len(legal_moves)==0:
            if l>m_max:
                m_max=l
            
            return m_max
        for m in legal_moves:
           
            game_state._active_player=player
            m_max=going_on(game_state.forecast_move(m),l+1,m_max)
        
        return m_max
        
    if len(game.get_blank_spaces())<=15:
        game_state=game.copy()
        x,y =game_state.get_player_location(player)
        
        m_max=going_on(game_state)
        
        return m_max
    else:
        own_moves = len(game.get_legal_moves(player))
        opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
        return float(own_moves - opp_moves)


def custom_score_4(game,player):
    """For details about the heuristic see heuristic_analysis.pdf

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    
    y, x = game.get_player_location(player)
    return float((3 - y)**2 + (3 - x)**2)

def custom_score_5(game,player):
    """For details about the heuristic see heuristic_analysis.pdf

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    
    y, x = game.get_player_location(player)
    return float(abs(3 - y) + abs(3 - x))

def custom_score_6(game,player):
    """For details about the heuristic see heuristic_analysis.pdf

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    def going_on(game_state,l=0,m_max=0):
        #print("begin")
        #print("l={}".format(l))
        legal_moves=game_state.get_legal_moves(player)
        #print("legal_moves: {}".format(legal_moves))
        if len(legal_moves)==0:
            if l>m_max:
                m_max=l
            #print("m_max={}".format(m_max))
            return m_max
        for m in legal_moves:
           # print("m: {}".format(m))
            game_state._active_player=player
            m_max=going_on(game_state.forecast_move(m),l+1,m_max)
        #print("max={}".format(m_max))
        return m_max
        
    if len(game.get_blank_spaces())<=15:
        game_state=game.copy()
        x,y =game_state.get_player_location(player)
        #print("x={},y={}".format(x,y))
        m_max=going_on(game_state)
        #print("final_max={}".format(m_max))
        return m_max
    
    y, x = game.get_player_location(player)
    return float(abs(3 - y) + abs(3 - x))

def custom_score_7(game,player):
    """For details about the heuristic see heuristic_analysis.pdf

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    
    y, x = game.get_player_location(player)
    return float((3 - y)**2 + (3 - x)**2)



def custom_score_8(game,player):
    """For details about the heuristic see heuristic_analysis.pdf

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    def going_on(game_state,l=0,m_max=0):
        #print("begin")
        #print("l={}".format(l))
        legal_moves=game_state.get_legal_moves(player)
        #print("legal_moves: {}".format(legal_moves))
        if len(legal_moves)==0:
            if l>m_max:
                m_max=l
            #print("m_max={}".format(m_max))
            return m_max
        for m in legal_moves:
           # print("m: {}".format(m))
            game_state._active_player=player
            m_max=going_on(game_state.forecast_move(m),l+1,m_max)
        #print("max={}".format(m_max))
        return m_max
        
    if len(game.get_blank_spaces())<=15:
        game_state=game.copy()
        x,y =game_state.get_player_location(player)
        #print("x={},y={}".format(x,y))
        m_max=going_on(game_state)
        #print("final_max={}".format(m_max))
        return m_max
    
    y, x = game.get_player_location(player)
    return float((3 - y)**2 +(3 - x)**2)

def custom_score_9(game,player):
    """For details about the heuristic see heuristic_analysis.pdf

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    y, x = game.get_player_location(player)
    d= float((3 - y)**2 + (3 - x)**2)/10.
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves)+d
    


def custom_score_10(game,player):
    """For details about the heuristic see heuristic_analysis.pdf

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    y, x = game.get_player_location(player)
    d= float((3 - y)**2 + (3 - x)**2)/10.
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves)-d
    
        
def check(x,y,blank,move_list,move_list2):
    """ helper function for custom_score_11"""
    l=0
    l2=0
    x1=x
    y1=y
    for u,v in move_list:
            x1=x1+u
            y1=y1+v
            if (x1,y1) in blank:
                l=l+1
            else:
                break
    if l!=7:
        x2=x
        y2=y
        for u,v in move_list2:
            x2=x2+u
            y2=y2+v
            if (x2,y2) in blank:
                l2=l2+1
            else:
                break
    return max(l,l2)


def custom_score_11(game,player):
    """For details about the heuristic see heuristic_analysis.pdf

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    
    
    blank=game.get_blank_spaces()
    x,y = game.get_player_location(player)
    
    a=[(2,1),(-2,1),(1,-2),(1,2),(-2,-1),(2,-1),(-1,2)]
    b=[(1, 2), (1, -2), (-2, 1), (2, 1), (-1, -2), (-1, 2), (2, -1)]
    c=[(2,-1),(-2,-1),(1,2),(1,-2),(-2,1),(2,1),(-1,-2)]
    d=[(1, -2), (1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2), (2, 1)]
    a2=[(-2, -1), (2, -1), (-1, 2), (-1, -2), (2, 1), (-2, 1), (1, -2)]
    b2=[(-1, -2), (-1, 2), (2, -1), (-2, -1), (1, 2), (1, -2), (-2, 1)]
    c2=[(-2, 1), (2, 1), (-1, -2), (-1, 2), (2, -1), (-2, -1), (1, 2)]
    d2=[(-1, 2), (-1, -2), (2, 1), (-2, 1), (1, -2), (1, 2), (-2, -1)]
    e=[(2,-1),(-1,2),(-1,-2),(2,1),(-2,1),(1,-2),(1,2)]
    f=[(2,1),(-1,-2),(-1,2),(2,-1),(-2,-1),(1,2),(1,-2)]
    e2=[(-2, -1), (1, 2), (1, -2), (-2, 1), (2, 1), (-1, -2), (-1, 2)]
    f2=[(-2, 1), (1, -2), (1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2)]
    g=[(1,-2),(-2,1),(2,1),(-1,-2),(-1,2),(2,-1),(-2,-1)]
    h=[(-1,-2),(2,1),(-2,1),(1,-2),(1,2),(-2,-1),(2,-1)]
    g2=[(1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2), (2, 1), (-2, 1)]
    h2=[(-1, 2), (2, -1), (-2, -1), (1, 2), (1, -2), (-2, 1), (2, 1)]

    l_max=0
    
    if (x+2<=6) and (y+2<=6):
        l=check(x,y,blank,a,b)
        if l>l_max:
            l_max=l
            
    if ((x+2<=6) and (y-2>=0)) and l_max!=7:
        l=check(x,y,blank,c,d)
        if l>l_max:
            l_max=l
        
    if ((x-2>=0) and (y-2>=0)) and l_max!=7:
        l=check(x,y,blank,a2,b2)
        if l>l_max:
            l_max=l
    
    if ((x-2>=0) and (y+2<=6)) and l_max!=7:
        l=check(x,y,blank,c2,d2)
        if l>l_max:
            l_max=l
            
    if ((x+2<=6)and((y+1<=6)and(y-1>=0))) and l_max!=7:
        l=check(x,y,blank,e,f)
        if l>l_max:
            l_max=l
        
    if ((x-2>=0)and((y+1<=6)and(y-1>=0))) and l_max!=7:
        l=check(x,y,blank,e2,f2)
        if l>l_max:
            l_max=l
                
    if ((y-2>=0)and((x+1<=6)and(x-1>=0))) and l_max!=7:
        l=check(x,y,blank,g,h)
        if l>l_max:
            l_max=l
        
    if ((y+2<=6)and((x+1<=6)and(x-1>=0))) and l_max!=7:
        l=check(x,y,blank,g2,h2)
        if l>l_max:
            l_max=l
        
                    
    return float(l_max)
    
def check_a(x,y,blank,move_list,move_list2):
    """helper function for custom_score_12"""    
    l=0
    l2=0
    x1=x
    y1=y
    for u,v in move_list:
            x1=x1+u
            y1=y1+v
            if (x1,y1) in blank:
                l=l+1
            else:
                break
   
    x2=x
    y2=y
    for u,v in move_list2:
        x2=x2+u
        y2=y2+v
        if (x2,y2) in blank:
            l2=l2+1
        else:
            break
    
    return l+l2


def custom_score_12(game,player):
    """For details about the heuristic see heuristic_analysis.pdf

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).

    Returns
    ----------
    float
        The heuristic value of the current game state.
    """    


    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    
    
    blank=game.get_blank_spaces()
    x,y = game.get_player_location(player)
    
    a=[(2,1),(-2,1),(1,-2),(1,2),(-2,-1),(2,-1),(-1,2)]
    b=[(1, 2), (1, -2), (-2, 1), (2, 1), (-1, -2), (-1, 2), (2, -1)]
    c=[(2,-1),(-2,-1),(1,2),(1,-2),(-2,1),(2,1),(-1,-2)]
    d=[(1, -2), (1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2), (2, 1)]
    a2=[(-2, -1), (2, -1), (-1, 2), (-1, -2), (2, 1), (-2, 1), (1, -2)]
    b2=[(-1, -2), (-1, 2), (2, -1), (-2, -1), (1, 2), (1, -2), (-2, 1)]
    c2=[(-2, 1), (2, 1), (-1, -2), (-1, 2), (2, -1), (-2, -1), (1, 2)]
    d2=[(-1, 2), (-1, -2), (2, 1), (-2, 1), (1, -2), (1, 2), (-2, -1)]
    e=[(2,-1),(-1,2),(-1,-2),(2,1),(-2,1),(1,-2),(1,2)]
    f=[(2,1),(-1,-2),(-1,2),(2,-1),(-2,-1),(1,2),(1,-2)]
    e2=[(-2, -1), (1, 2), (1, -2), (-2, 1), (2, 1), (-1, -2), (-1, 2)]
    f2=[(-2, 1), (1, -2), (1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2)]
    g=[(1,-2),(-2,1),(2,1),(-1,-2),(-1,2),(2,-1),(-2,-1)]
    h=[(-1,-2),(2,1),(-2,1),(1,-2),(1,2),(-2,-1),(2,-1)]
    g2=[(1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2), (2, 1), (-2, 1)]
    h2=[(-1, 2), (2, -1), (-2, -1), (1, 2), (1, -2), (-2, 1), (2, 1)]

    l_sum=0
    
    if (x+2<=6) and (y+2<=6):
        l=check_a(x,y,blank,a,b)
        l_sum=l_sum+l
        
    if ((x+2<=6) and (y-2>=0)):
        l=check_a(x,y,blank,c,d)
        l_sum=l_sum+l
        
    if ((x-2>=0) and (y-2>=0)):
        l=check_a(x,y,blank,a2,b2)
        l_sum=l_sum+l
        
    if ((x-2>=0) and (y+2<=6)):
        l=check_a(x,y,blank,c2,d2)
        l_sum=l_sum+l
        
    if ((x+2<=6)and((y+1<=6)and(y-1>=0))):
        l=check_a(x,y,blank,e,f)
        l_sum=l_sum+l
        
    if ((x-2>=0)and((y+1<=6)and(y-1>=0))):
        l=check_a(x,y,blank,e2,f2)
        l_sum=l_sum+l
        
    if ((y-2>=0)and((x+1<=6)and(x-1>=0))):
        l=check_a(x,y,blank,g,h)
        l_sum=l_sum+l
        
    if ((y+2<=6)and((x+1<=6)and(x-1>=0))):
        l=check_a(x,y,blank,g2,h2)
        l_sum=l_sum+l
                    
    return float(l_sum)


def custom_score_13(game,player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    blank=game.get_blank_spaces()
    
    if len(blank)>=30:
        x,y = game.get_player_location(player)
        return float((3 - y)**2 + (3 - x)**2)
    else:
        x,y = game.get_player_location(player)
    
        a=[(2,1),(-2,1),(1,-2),(1,2),(-2,-1),(2,-1),(-1,2)]
        b=[(1, 2), (1, -2), (-2, 1), (2, 1), (-1, -2), (-1, 2), (2, -1)]
        c=[(2,-1),(-2,-1),(1,2),(1,-2),(-2,1),(2,1),(-1,-2)]
        d=[(1, -2), (1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2), (2, 1)]
        a2=[(-2, -1), (2, -1), (-1, 2), (-1, -2), (2, 1), (-2, 1), (1, -2)]
        b2=[(-1, -2), (-1, 2), (2, -1), (-2, -1), (1, 2), (1, -2), (-2, 1)]
        c2=[(-2, 1), (2, 1), (-1, -2), (-1, 2), (2, -1), (-2, -1), (1, 2)]
        d2=[(-1, 2), (-1, -2), (2, 1), (-2, 1), (1, -2), (1, 2), (-2, -1)]
        e=[(2,-1),(-1,2),(-1,-2),(2,1),(-2,1),(1,-2),(1,2)]
        f=[(2,1),(-1,-2),(-1,2),(2,-1),(-2,-1),(1,2),(1,-2)]
        e2=[(-2, -1), (1, 2), (1, -2), (-2, 1), (2, 1), (-1, -2), (-1, 2)]
        f2=[(-2, 1), (1, -2), (1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2)]
        g=[(1,-2),(-2,1),(2,1),(-1,-2),(-1,2),(2,-1),(-2,-1)]
        h=[(-1,-2),(2,1),(-2,1),(1,-2),(1,2),(-2,-1),(2,-1)]
        g2=[(1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2), (2, 1), (-2, 1)]
        h2=[(-1, 2), (2, -1), (-2, -1), (1, 2), (1, -2), (-2, 1), (2, 1)]
    
        l_sum=0
        
        if (x+2<=6) and (y+2<=6):
            l=check_a(x,y,blank,a,b)
            l_sum=l_sum+l
            
        if ((x+2<=6) and (y-2>=0)):
            l=check_a(x,y,blank,c,d)
            l_sum=l_sum+l
            
        if ((x-2>=0) and (y-2>=0)):
            l=check_a(x,y,blank,a2,b2)
            l_sum=l_sum+l
            
        if ((x-2>=0) and (y+2<=6)):
            l=check_a(x,y,blank,c2,d2)
            l_sum=l_sum+l
            
        if ((x+2<=6)and((y+1<=6)and(y-1>=0))):
            l=check_a(x,y,blank,e,f)
            l_sum=l_sum+l
            
        if ((x-2>=0)and((y+1<=6)and(y-1>=0))):
            l=check_a(x,y,blank,e2,f2)
            l_sum=l_sum+l
            
        if ((y-2>=0)and((x+1<=6)and(x-1>=0))):
            l=check_a(x,y,blank,g,h)
            l_sum=l_sum+l
            
        if ((y+2<=6)and((x+1<=6)and(x-1>=0))):
            l=check_a(x,y,blank,g2,h2)
            l_sum=l_sum+l
                        
        return float(l_sum)
    



    
        
class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    
    
    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        def MIN_VALUE(state,self,d,depth):
            if self.time_left() < self.TIMER_THRESHOLD:
                 raise SearchTimeout()
            if not state.get_legal_moves() or d==depth:
                return self.score(state,self)
            legal=state.get_legal_moves()
            v=min([MAX_VALUE(state.forecast_move(m),self,d+1,depth) for m in legal])
            return v
               
        def MAX_VALUE(state,self,d,depth):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            if not state.get_legal_moves() or d==depth:
                return self.score(state,self)
            legal=state.get_legal_moves()
            v=max([MIN_VALUE(state.forecast_move(m),self,d+1,depth) for m in legal])
            return v

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return (-1, -1)
        _, move = max([(MIN_VALUE(game.forecast_move(m),self,1,depth),m) for m in legal_moves])
        
        
        
        return move

        # TODO: finish this function!
        #raise NotImplementedError


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """
    isHuman = False
    
    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left
        
         # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        is_time=True
        my_depth=0
        while is_time:
            try:
                # The try/except block will automatically catch the exception
                # raised when the timer is about to expire.
                best_move= self.alphabeta(game, my_depth)
                if best_move==(-1,1):
                    return best_move
                my_depth=my_depth+1
    
            except SearchTimeout:
                is_time=False
                pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move


        # TODO: finish this function!
        raise NotImplementedError

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        
        
        
        def MIN_VALUE(state,self,d,depth,alpha,beta):
            if self.time_left() < self.TIMER_THRESHOLD:
                 raise SearchTimeout()
            if not state.get_legal_moves() or d==depth:
                return self.score(state,self)
            legal=state.get_legal_moves()
            w=float("+inf")
            for m in legal:
                w_prime=MAX_VALUE(state.forecast_move(m),self,d+1,depth,alpha,beta)
                w=min(w,w_prime)
                if w<=alpha:
                    return w
                beta=min(beta,w)
            return w
               
        def MAX_VALUE(state,self,d,depth,alpha,beta):
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            if not state.get_legal_moves() or d==depth:
                return self.score(state,self)
            legal=state.get_legal_moves()
            w=float("-inf")
            for m in legal:
                w_prime=MIN_VALUE(state.forecast_move(m),self,d+1,depth,alpha,beta)
                w=max(w,w_prime)
                if w>=beta:
                    return w
                alpha=max(alpha,w)
            return w
        
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
            
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return (-1, -1)
        
        if depth==0:
            return legal_moves[0]
        
        v=float("-inf")
        move=legal_moves[0]
        for m in legal_moves:
            v_prime=MIN_VALUE(game.forecast_move(m),self,1,depth,alpha,beta)
            if v_prime>v:
                 v=v_prime
                 move=m
            alpha=max(alpha,v)    
         
        return move    