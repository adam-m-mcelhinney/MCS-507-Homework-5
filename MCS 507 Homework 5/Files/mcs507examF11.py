# L-19 MCS 507 Wed 10 Oct 2012 : mcs507examF11.py

# This script solves the in-class version of the midterm exam of Fall 2011.

def first_equation_solution(L):
   """
   Returns the expansion of the convergents
   in the list L.
   """
   k = len(L)-1;
   r = L[k]
   while(k > 0):
      r = L[k-1] + 1.0/r
      k = k - 1
   return r

def first_question():
   """
   A continued fraction approximation for sqrt(2) is
          1
   1 + -----------
        2 +   1
            ------
            2 + ...
 
   The list of convergents in the continued fraction expansion
   of sqrt(2) is [1,2,2,2,2,...,2].

   Give the definition of a Python function which takes on input
   a list L of convergents and returns the floating point approximation
   (of type float) defined by the continued fraction expansion given by L.
   """
   L = [1,2,2,2,2,2,2,2,2,2,2]
   e = first_equation_solution(L)
   print e
   print e**2
   ans = raw_input('hit enter to continue')

def second_question_solution():
   """
   Computes the Taylor series with sympy of
   f(x) = exp(sin(2*pi*x)) about x = 0.5
   for 2, 3, 4, and 5 terms and compares
   the evaluated series with f(0.6).
   """
   import sympy as sp
   x = sp.var('x')
   f = sp.exp(sp.sin(2*sp.pi*x))
   s = f.series(x,x0=0.5,n=None)
   t = [s.next() for i in xrange(5)]
   print t
   u = [sum(t[0:k]) for k in xrange(2,6)]
   print u
   e = [sp.Subs(s,(x),(0.6)).doit() for s in u]
   e16 = [n.evalf(16) for n in e]
   print e16
   vf = sp.Subs(f,(x),(0.6)).doit() 
   vf16 = vf.evalf(16)
   print vf16
   error = [e - vf16 for e in e16]
   print error

def second_question():
   """
   Consider the expression f(x) = exp(sin(2*pi*x))
   Write sympy code to compute Taylor series of f(x) about x = 0.5,
   series with 2, 3, 4, and 5 terms.
   Give code to evaluate the series at 0.6 and to compare with f(0.6).
   """
   second_question_solution()
   ans = raw_input('hit enter to continue')

def third_question_solution():
   """
   Generates a random 100-by-100 matrix,
   with elements normally distributed with mean 0
   and standard deviation 1 using numpy.
   The eigenvalues of this random matrix
   are plotted with pyplot.
   """
   import numpy as np
   from random import randint
   from matplotlib import pyplot as plt
   f = lambda i,j: np.random.normal(0*i,0*j+1)
   A = np.fromfunction(f,(100,100))
   # print A
   v = np.linalg.eig(A)
   print 'the eigenvalues :', v[0]
   L = list(v[0])
   x = [c.real for c in L]
   y = [c.imag for c in L]
   print 'see the plot ...'
   plt.plot(x,y,'bo')
   plt.show()

def third_question():
   """
   Give Python code for the following:
   (1) Generate a random 100-by-100 matrix with random elements,
       normally distributed with mean 0 and standard deviation 1
       using normal of the random module of numpy.
   (2) Plot the eigenvalues with pyplot or pylab.
   """
   third_question_solution()

def per(A,k,L,prod):
   """
   Row expansion for the permanent of A.
   The counter k is the current column and
   L contains the indices of the selected rows.
   """
   if k == A.shape[1]:
      print L, prod
      return prod
   else:
      sum = 0
      for i in range(A.shape[0]):
         if not i in L:
            sum = sum + per(A,k+1,L+[i],prod*A[i,k])
      return sum

def permanent(A):
   """
   Returns the permanent of the matrix A.
   """
   return per(A,0,[],1)

def fourth_question_solution():
   """
   Test on the permanent.
   """
   import numpy as np
   n = 4
   A = np.random.random_integers(0,1,size=(n,n))
   print A
   p = permanent(A)
   print 'permanent :', p

def fourth_question():
   """
   Given an n-by-n matrix A, the permanent of the matrix is
   the sum of the products A[i,s[i]], for i = 1,2,..,n,
   where the sum runs over all permutations s of (1,2,..,n).
   The expansion formula for the permanent above is very similar
   to the row expansion formula for the determinant, except for
   the sign changes, which are absent in the permanent expansion.
   Write a Python function permanent that takes on input
   a matrix and that returns the permanent of the matrix.
   An auxiliary recursive function uses the expansion formula
   above to compute the permanent.
   """
   fourth_question_solution()
   ans = raw_input('hit enter to continue')

def main():
   """
   Runs through the solutions of the four questions.
   Because of the plot in question 3, question 3 runs last.
   """
   print 'question 1 :'
   print first_question.__doc__
   print 'running the solution to question 1...'
   first_question()
   print 'question 2 :'
   print second_question.__doc__
   print 'running the solution to question 2...'
   second_question()
   print 'question 4 :'
   print fourth_question.__doc__
   print 'running the solution to question 4...'
   fourth_question()
   print 'question 3 :'
   print third_question.__doc__
   print 'running the solution to question 3...'
   third_question()

if __name__=="__main__": main()
