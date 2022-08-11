# Sieve of Eratosthenes

## Video Demo: <https://youtu.be/CVsvUFaEUUc>

## Description:
> The purpose of the Sieve of Eratosthenes is to output a list of prime numbers, given an input N, where N is a positive integer.

## The Steps:
### Generating a valid Input
> in the first function get_input, the function will request the user to input a positive integer and raise a ValueError for any number smaller than 2. The reason being that
> 2 i the smallest possible prime number in existence.

### Creating an Integer List
> After the input of N, the functions create_integer_list will generate a list of integers from 2 to N. the values 0 and 1 are manually removed via a naive flow.

### The Sieve
> The sieve comes in two sub-parts

#### The Composite List Generator
> typical pseudo code for Eratosthenes requirea that a floor square root is generated for input N, and that it is necessary and sufficient to check all numbers lesser than
> sqrt(N). In this algorithm, I have a nested for loop to input all composite numbers into a blank list. The problem arises when this list contains repeated digits and also
> not properly ordered.

#### The Sorter
> the next sub-part contains a naive sorter to remove repeated entries, and also arrange the entries in increasing order. This error was spotted during unit testing.

### The Composite Remover
> The final step would be to remove all composite numbers from the original integer list.

### Final Notes
> I believe my code does not fully display Eratosthene's approach, and I might have used Euler's approach subtly.

> END