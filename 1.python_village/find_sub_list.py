# This is to find a sublist within a list
def array123(nums):
  pattern = [1,2,3]
  matches = []
  for i in range(len(nums)):
    if nums[i] == pattern[0] and nums[i:i+len(pattern)] == pattern:
      matches.append(pattern)
  if len(matches) != 0:
    return(True)
  else:
    return(False)
