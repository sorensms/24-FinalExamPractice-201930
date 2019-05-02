"""
PRACTICE Exam 3.

This problem provides practice at:
  ***  LOOPS WITHIN LOOPS, SEQUENCES and MUTATION  ***

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Madie Sorensen.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_zero_changer()


def run_test_zero_changer():
    """ Tests the    zero_changer    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   zero_changer   function:')
    print('--------------------------------------------------')

    # Test 1:
    test1 = ([8, 4, 0, 9], [77, 0, 0, 1, 5, 0], [4, 4, 4], [4, 0, 4])
    expected1 = ([8, 4, 1, 9], [77, 2, 3, 1, 5, 4], [4, 4, 4], [4, 5, 4])
    zero_changer(test1)
    print()
    print('Test 1:')
    print('  Expected:', expected1)
    print('  Actual:  ', test1)

    # Test 2:
    test2 = ([16, 0, 0, 4], [0, 0, 0, 0, 0], [12, 9,0, 4], [6,0,0, 0, 4])
    expected2 = ([16, 1, 2, 4], [3, 4, 5, 6, 7], [12, 9, 8, 4], [6, 9, 10, 11, 4])
    zero_changer(test2)
    print()
    print('Test 2:')
    print('  Expected:', expected2)
    print('  Actual:  ', test2)

    # Test 3:
    test3 = ([12, 5, 2, 1,6], [9,8,18, 0, 0, 1, 5, 0], [6, 9, 8], [6, 0,0,5, 4])
    expected3 = ([12, 5, 2, 1, 6], [9, 8, 18, 1, 2, 1, 5, 3], [6, 9, 8], [6, 4, 5, 5, 4])
    zero_changer(test3)
    print()
    print('Test 3:')
    print('  Expected:', expected3)
    print('  Actual:  ', test3)

    # -------------------------------------------------------------------------
    # Done: 2. Write at least 2 additional tests for the
    #    zero_changer
    # function.  Try to choose some unexpected things like empty lists
    # or an empty tuple, or a list with no zeros, etc.
    # -------------------------------------------------------------------------


def zero_changer(tuple_of_lists):
    a=1
    for k in range (len(tuple_of_lists)):
        inside=tuple_of_lists[k]
        for m in range(len(tuple_of_lists[k])):
            if inside[m]==0:
                inside[m]=a
                a=a+1

    """
    What comes in:  A TUPLE of LISTs,
                    where the interior lists contain only integers.
    What goes out:  Nothing (i.e., none)
    Side effects:  The argument is MUTATED so that:
      -- the 1st 0 in the given tuple of lists is changed to 1.
      -- the 2nd 0 in the given tuple of lists is changed to 2.
      -- the 3rd 0 in the given tuple of lists is changed to 3.
           etc.
    Example:
      If the given tuple of lists is:
          ([8, 4, 0, 9], [77, 0, 0, 1, 5, 0], [4, 4, 4], [4, 0, 4])
      then AFTER this function is called with that tuple of lists,
      the tuple of lists has been MUTATED to:
          ([8, 4, 1, 9], [77, 2, 3, 1, 5, 4], [4, 4, 4], [4, 5, 4])
    Note that:
      -- If there are no zeros in the given tuple of lists,
           then this function does nothing.
      -- After this function call, the tuple of lists IN THE CALLER
           should contain no zeros.
    Type hints:
      :type tuple_of_lists: tuple of list[int]
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:  10 minutes.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
