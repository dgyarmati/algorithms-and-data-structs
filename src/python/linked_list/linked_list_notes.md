###questions to ask:
1. error handling?

###implementation:
1. you will probably need a 
	- Node with data and next pointer
	- a LinkedList wrapper with a head
2. deal with missing head
	
###methods:
1. append: watch out for the head
2. delete:
	- delete head or
	- keep track of previous node
3. delete duplicates:
	- iterative: (O N speed, O 1 space)
		- use set as buffer and keep track of previous
	- recursive: (O N^2 speed)
		- have 2 pointers
4. kth to last:
	iterative:
		- 2 pointers, move the first one to k, then move both until first is not None, return second
	recursive:
		- print:
			- base case: node is None, otherwise call the method again and increment with 1, if index equals given, print, else return idx
5. delete middle w/o knowing the head:
	- just take the node and reassign next (after checks)
6. partition:
    - create two lists, one for less than x, other for greater or eq. to x, and merge the two in the end
    or: elements bigger than pivot are put to the tail, smaller are at the head; each time we insert an element, we update the head or the tail
7. sum:
    - implement addition recursively
    - comparing lengths: pad shorter with zeroes
	