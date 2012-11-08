# L-20 MCS 507 Fri 12 Oct 2012 : stirling.py

# The Stirling numbers of the first kind c(n,k) satisfy the recurrence
# c(n,k) = - (n-1) c(n-1,k) + c(n-1,k-1), for n >= 1 and k >= 1,
# with the initial conditions that c(n,k) = 0 
# if n <= 0 or k <= 0, except c(0,0) = 1.

# Write a Python function that takes on input n and k
# and that returns a dictionary with as keys the tuples (n,k)
# and values the corresponding Stirling numbers for all tuples
# computed in the recurrence.

D = {}

def stirling(n,k):
   """
   Computes the Stirling numbers using a dictionary.
   """
   if D.has_key((n,k)):
      return D[(n,k)]
   if ((n == 0) and (k == 0)):
      D[(0,0)] = 1; return 1
   elif (n <= 0):
      D[(n,k)] = 0; return 0
   elif (k <= 0):
      D[(n,k)] = 0; return 0
   else:
      D[(n,k)] = -(n-1)*stirling(n-1,k) + stirling(n-1,k-1)
      return D[(n,k)]

def main():
   """
   interactive test on stirling
   """
   n = input('give n : ')
   k = input('give k : ')
   print stirling(n,k)
   print D

main()
