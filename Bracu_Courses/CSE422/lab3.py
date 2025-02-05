#part 1
def Mortal_Kombat(starting):
    def minimax_pruning(node,moves_left,alpha,beta,maximising_score):
        if moves_left==0 or node["ck"]:
            return node["score"]
        if maximising_score:
            highest_score=-float('inf')
            for i in node["branch"]:
                score=minimax_pruning(i,moves_left - 1,alpha,beta,False)
                highest_score=max(highest_score,score)
                alpha=max(alpha,score)
                if alpha>=beta:
                    break
            return highest_score
        else:
            lowest_score=float('inf')
            for i in node["branch"]:
                score=minimax_pruning(i,moves_left - 1,alpha,beta,True)
                lowest_score=min(lowest_score,score)
                beta=min(beta, score)
                if alpha>=beta:
                    break
            return lowest_score

    g_dictionary={
        "score":None,
        "ck":False,
        "branch":[
            {"score":-1, "ck":True, "branch":[]},
            {"score":1, "ck":True, "branch":[]},
            {"score":-1, "ck":True, "branch":[]},
            {"score":1, "ck":True, "branch":[]},
        ]
    }
    resulting_score=minimax_pruning(g_dictionary,5,-float('inf'),float('inf'),starting==0)
    winner="Scorpion" if resulting_score==-1 else "Sub-Zero"

    rounds=7
    round_winners=[]
    for i in range(rounds):
        maximize =(i%2==0) if starting ==0 else (i%2!=0)
        round_score=minimax_pruning(g_dictionary,5,-float('inf'),float('inf'),maximize)
        winner ="Scorpion" if round_score==-1 else "Sub-Zero"
        round_winners.append(winner)

    print(f"final winner:{winner}")
    print(f"round numbers:{rounds}")
    for round_num, winner in enumerate(round_winners,start=1):
        print(f"round-winner {round_num}:{winner}")

Mortal_Kombat(0)


#part2
def pacman_simulation(cost):
    def evaluate_position(position,depth,is_max_player):
        if depth == 0 or position.get("terminal",False):
            return position.get("score",0)

        if is_max_player:
            return max(evaluate_position(child,depth-1,False) for child in position.get("next",[]))
        else:
            return min(evaluate_position(child,depth-1,True) for child in position.get("next",[]))

    g_dictionary = {
        "score": None,
        "terminal": False,
        "next": [
            {"score": 8, "terminal": True},
            {"score": 5, "terminal": True},
            {"score": 3, "terminal": True},
            {"score": 9, "terminal": True}
        ]
    }
    
    base_score=evaluate_position(g_dictionary,3,True)

    outcome1=max(g_dictionary["next"][0]["score"],g_dictionary["next"][1]["score"])-cost
    outcome2=max(g_dictionary["next"][2]["score"],g_dictionary["next"][3]["score"])-cost

    print(f"without dark magic:{base_score}")
    if max(outcome1,outcome2)>base_score:
        print(f"with dark magic:{max(outcome1,outcome2)}")
    else:
        print("Dark magic don't give advantage.")

pacman_simulation(2)
