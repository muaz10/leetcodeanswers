def implement_str_str(haystack: str, needle: str):
  lhay=len(haystack)
  lnee=len(needle)

  if(lhay<lnee):
    return -1
  if(haystack==needle or needle==""):
    return 0
  
  for i in range(0, lhay-lnee+1, 1):
    candidate=haystack[i:i+lnee]
    if(candidate==needle):
      return i

  return -1

haystack = "hello"
needle = "h"
print(implement_str_str(haystack, needle))