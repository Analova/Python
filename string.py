emoji="\U0001FO8“
name="Cidny"
team="Bulls"
record=4



# senctence= "Hi my name is %s and I don\'t like the %s %s because they won %s times" %(name,team,emoji,4)

senctence= f"Hi my name is {name[0]} and I don\'t like the {team} {'.' * record}\n  {emoji} because they won {record} times"
print(senctence)