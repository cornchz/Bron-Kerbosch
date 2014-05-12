## What is this?

Performance comparison of three Bron–Kerbosch algorithm implementations that find all maximal cliques in a graph. 

## Implementations

* **Ver1:** naive Bron–Kerbosch algorithm
* **Ver2:** Ver1 with pivot
* **Ver3:** Ver2 with degeneracy ordering

## Run

    python maximal_cliques.py

## Result

Stdout result for the sample data

    ## Naive Bron–Kerbosch algorithm
    26 recursive calls
    0: [1, 2, 3, 4]
    1: [2, 3, 5]
    2: [5, 6, 7]

    ## Bron–Kerbosch algorithm with pivot
    14 recursive calls
    0: [1, 2, 3, 4]
    1: [5, 2, 3]
    2: [5, 6, 7]

    ## Bron–Kerbosch algorithm with pivot and degeneracy ordering
    19 recursive calls
    0: [6, 5, 7]
    1: [5, 2, 3]
    2: [1, 2, 3, 4]

## Time Comlexity

Worst-case time-complexity analysis is [here](http://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm#Worst-case_analysis).

## License

[BSD License](http://opensource.org/licenses/BSD-3-Clause)
