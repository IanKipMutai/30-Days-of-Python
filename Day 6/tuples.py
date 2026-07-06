tpl = ()
tpl = tuple()

brothers = ('Ryan', 'Joel','David','Moses')
sisters = ('Faith','Joy','Mercy','Esther')
siblings = brothers + sisters
print(len(siblings))

family_members = list(siblings)
family_members.append('Kimutai')
family_members.append('Caren')
print(family_members)

siblings = family_members[0:len(family_members)-2]
parents = family_members[len(family_members)-2:len(family_members)]
print(siblings)
print(parents)