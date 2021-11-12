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


