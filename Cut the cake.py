# https://www.codewars.com/kata/586214e1ef065414220000a8/train/python
def cut(cake):
    sample_cut = [s for s in cake if s]
    def num_raisins(cake):
        count=0
        for i in cake:
            for j in i:
                if j=="o":
                    count+=1
        return count
    n=num_raisins(sample_cut)
    def cut_cake_horizontal(lst,which_row):
        a=lst[:which_row]+lst[which_row+1:]
        return a
    def cut_cake_vertical(lst,which_col):
        a=lst[:which_col]+lst[which_col+1:]
        return a
    while True:
        while num_raisins(sample_cut)>n/2:
            for i in range(len(sample_cut)):
                if num_raisins(cut_cake_horizontal(sample_cut,i))>=n/2:
                    sample_cut=cut_cake_horizontal(sample_cut,i)
                    break
            for i in range(len(sample_cut[0])):
                if num_raisins(cut_cake_vertical(sample_cut,i))>=n/2:
                    sample_cut=cut_cake_vertical(sample_cut,i)
                    break
        return sample_cut
    return []

# INCOMPLETED