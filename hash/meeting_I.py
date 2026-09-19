def meeting_I(intervals):
  if not intervals:
    return True

  intervals.sort()
  prev_e = -1
  for s,e in intervals:
    if prev_e > s:
      return False
    else:
      prev_e = e

  return True

inter = [[1,3],[4,7],[0,8]]
print(meeting_I(inter))
