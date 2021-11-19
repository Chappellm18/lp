# Knuth Order

NRE -> RE -> Resursive Langauges -> Context Sensitive L -> Context Free L -> Regular Langauges

## Formal System 

- Axioms 
- Rules of Inference
- Theorem

### Example

P 

P -> q      
_______
Therefore q <-- modus ponens

a+b = b+a

## Consistent

- if you can prove that P is true and P is not true it doesnt work

### Example

p = true         |       2=3

p = not true     |       2=2

## Godel Incompleteness Theorem

- if you have a consistent formal system is it incomplete

## Lab problem
Show no matter how they split up a rule will be broken
3 properites (key idea)


# Chapter 18 stuff
- bad: gets new temp everytime you need a temp

* when add, mul, assign, print: if one of the values is a temp remove one from temp count
* Constant folding: do calculations at assemble time?? -> ( x = 2 + 3 ) => ( x = 5) -> folding





# Grid - list of all turing machines example

    1   10  11  100 101 110 111 1000
T1  A   A   R   A   R   R   A   A
T2  R   R   R   R   R   R   R   R
T3  A   A   A   A   A   A   A   A
T4  A   R   A   R   A   R   A   R

take the diagonal and flip it:
    not recurisvly enumerable


bb(n) -> n state TMs -> start on blank tape

mbb(n) -> n state TMs

f(n) = n + 1


# Chapter 20

AST -> Abstract Structure Tree

# pumping

S = uvwxy
    uv^iwx^iy = L
    |vwx| < L
    |vx| > 0

# Turing Machine
________________________________________
    T # W 
________________________________________
--T to H'--
T halts on W 
then
H' Loops
________________________________________
    H' # W 
________________________________________
--H' to H''--
H'' has a front end
T => [T] # T
[T] -> simulates H'
________________________________________
    H'' # H'' 
________________________________________



# sUCCESSOR fUNCTIONS

s(x) = x + 1


## def of addition
+(x,y) = x              for y = 0
+(x,s(y)) = s(+(x,y))   for y > 0


## def of mult
*(x,y) = 0              for y = 0
*(x,s(y)) = +( *(x,y))  for y > 0

* Primitive Recursion
* Ackermann's Function

Computable Functions
    
    |-> ackermann
    |    |
    |    |-> function
    |
    |
    |-> primitives
    |    |
    |    |-> addition
    |    |
    |    |-> multiplication
    |    |
    |    |-> ect.
    |

# c code

|
|   sheeeeet we out here writing c ?? 
|

## add function
int add(int x, int y) {
    if (y == 0) {
        return x;
    } else {
        return add(x, y - 1) + 1;
    }
}
## main function
int main() {
    printf("%d\n", add(2, 3));
    return 0;
}


## Ackermann's Function
A(x,y) = y + 1              for x = 0
A(x,y) = A(x-1, 1)          for x > 0 and y = 0
A(x,y) = A(x-1, A(x,y-1))   for x > 0 and y > 0

There is no primitive for this function

Call the function with
0,0
1,1
2,2
... until it breaks

def ackermann(x,y) {
    if (x == 0) {
        return y + 1;
    } else if (y == 0) {
        return ackermann(x - 1, 1);
    } else {
        return ackermann(x - 1, ackermann(x, y - 1));
    }
}


# Halting stuff again (proof that it dont exist)

p -->   |               | --> "Halt" (h halts)
        |      H'       |
w -->   |_______________| --> "Loop" (h halts)


"Halt" -> while(true) {infitine loop};


duplicate
        |       | - p -> |     | --> H' halts
p -->   |  dup  |        |  H' |
        |_______| - p -> |_____| --> H' loops

What happens when the input p is changed to H''

Not solveable

