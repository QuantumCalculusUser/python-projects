#https://www.codewars.com/kata/55dcdd2c5a73bdddcb000044/train/python
def calculate(rectangles):
    if not rectangles:
        return 0
    events = []
    for x1, y1, x2, y2 in rectangles:
        events.append((x1, 1, y1, y2))
        events.append((x2, -1, y1, y2))
    events.sort()
    active = []
    area = 0
    prev_x = events[0][0]
    for x, typ, y1, y2 in events:
        dx = x - prev_x
        if dx:
            intervals = sorted(active)
            covered_y = 0
            if intervals:
                s, e = intervals[0]
                for ns, ne in intervals[1:]:
                    if ns <= e:
                        e = max(e, ne)
                    else:
                        covered_y += e - s
                        s, e = ns, ne
                covered_y += e - s
            area += covered_y * dx
        if typ == 1:
            active.append((y1, y2))
        else:
            active.remove((y1, y2))
        prev_x = x
    return area