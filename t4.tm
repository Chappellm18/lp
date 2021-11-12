0             Start state
{5}           Set of final states

0 _ _ R 5     Use state 0 to check for ^ input
0 a x R 2

1 a x R 2     mark a
2 a a R 2     now move right to matching b
2 y y R 2

2 b y R 3     mark matching b
2 b b R 2     now move right to matching c
3 w w R 3

2 c x R 3     mark matching c
3 x x R 3     nox move left first marked a
3 c c R 3

3 x x R 1     start cycle again

1 x x R 4     check if all a's have been marked
4 x x R 4
4 _ _ R 5     if all a's marked, go to final state 5

1 y y R 4     check if all b's have been marked
4 y y R 4
4 _ _ R 5     if all b's marked, go to final state 5

1 x x R 4     check if all c's have been marked
4 x x R 4
4 _ _ R 5     if all c's marked, go to final state 5
