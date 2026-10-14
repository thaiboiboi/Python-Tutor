weight = [30, 10, 20]
value = [50 , 100 ,70]
capacity = 50
def all_posibilities(n):
    if (n==0):
        return [[]]
    else:
        lst_one_less = all_posibilities(n-1)
        lst1 = [[1] + lst1 for lst1 in lst_one_less]
        lst0 = [[0] + lst0 for lst0 in lst_one_less]
        return lst1 + lst0

lst_all_pos = all_posibilities(3)
tot_w =0
tot_v = 0
max_v = 0
for choice in lst_all_pos:
    tot_w=sum([v*weight[i] for i, v in enumerate(choice)])
    tot_v=sum([v*value[i] for i, v in enumerate(choice)])
    if ((tot_w<=capacity) & (tot_v>max_v)):
        optimal_choice = choice
        max_v = tot_v
print("The optimal choice is: ", optimal_choice)
print("Maximum value: ", max_v)
