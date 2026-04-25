#https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python
def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        count = 1
        while h * bounce > window:
            count += 2
            h *= bounce
        return count
    return -1