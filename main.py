"""This problem was asked by Google.
Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other
queue. This should be done in-place.
Recall that you can only push(item) or pop() from a stack, and enqueue(item) or dequeue() from a queue.
For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4],
 it should become [1, 4, 2, 3].
Hint: Try working backwards from the end state."""

import itertools


def interleave(stack):
    answer = [item for t in
              list(itertools.zip_longest(stack[0:len(stack) // 2], list(reversed(stack[len(stack) // 2::])))) for item
              in t if item]
    return answer


print(interleave([1, 2, 3, 4, 5]))
