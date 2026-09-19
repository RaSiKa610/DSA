import heapq

def meeting_II(intervals):
  if not intervals:
    return 0

  intervals.sort()
  free_rooms = []
  heapq.heappush(free_rooms, intervals[0][1])
  for i in range(1, len(intervals)):
    if free_rooms[0] <= intervals[i][0]:
      heapq.heappop(free_rooms)

    heapq.heappush(free_rooms, intervals[i][1])

  return len(free_rooms)


inter = [[0,30],[15,20],[1,4],[5,10]]
print(meeting_II(inter))
