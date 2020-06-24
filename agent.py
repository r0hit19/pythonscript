import random

# Function for taking the input
def entry(n):
    agent={}
    for i in range(1,n+1):
        name=input("enter the name of agent no. "+str(i)+":")
        avail=input("agent available or not(yes/no):").lower()
        if avail=='yes':
            is_available=1
        else:
            is_available=0
        if is_available==1:
            available_since=int(input("since when the agent is idle(in minutes):"))
        else:
            available_since=0
        role=input("role of the agent")
        agent[name]={'is_available':is_available,'available_since':available_since,'role_of_the_agent':role}
    return agent

#Agent selecetion mode(  ALL AVAILABLE MODE  )

def all_available_mode(names,roles):
    list=[]
    for id in names:
        if names[id]['is_available']==1 and names[id]['role_of_the_agent']==roles:
            list.append(id)


    return list


#Agent selection mode(   LEAST BUSY MODE   )
def least_busy_mode(agentdict,roles):
    l=[]
    m=0
    for id in agentdict:
        if agentdict[id]['is_available']==1 and agentdict[id]['role_of_the_agent']==roles:
            m=agentdict[id]['available_since']
            break
    for id in agentdict:
        if agentdict[id]['is_available'] == 1 and agentdict[id]['role_of_the_agent'] == roles:

            if agentdict[id]['available_since']>=m:
                l=[id]
    return l


#Agent selection mode(   RANDOM  MODE   )

def random_agent(agent_name,roles):
    s=[]
    for id in agent_name:
        if agent_name[id]['role_of_the_agent']==roles:
            s.append(id)

    return random.choice(s)

# MAIN FUNCTION
if __name__=="__main__":
    number=int(input("enter the number of agents"))
    agent=entry(number)
    print("list of all agents")
    print(agent)

    roles=input("enter the role ")
    print("select the mode of selection")
    w=1
    while w==1:
        select=int(input("enter 1. for all_available_mode......."
                         "enter 2. for least_busy_mode......."
                         "enter 3. random_agent_mode......."
                         "enter any other key to exit......"))

        if select==1:
            print("list of all available agents")
            list_available_agents=all_available_mode(agent,roles)
            print(list_available_agents)
        elif select==2:
            print("list of all least busy agents")
            l=least_busy_mode(agent,roles)
            print(l)
        elif select==3:
            print("randomly selected agent")
            l1 = random_agent(agent,roles)
            print(l1)
        else:
            w=2

