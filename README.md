╒════════════════════╤═══════════════════════════╤═══════════════════════════╤═══════════════════════════╤═══════════════════════════╕
│ Algorithm │ Real Substring (Text 1) │ Fake Substring (Text 1) │ Real Substring (Text 2) │ Fake Substring (Text 2) │
╞════════════════════╪═══════════════════════════╪═══════════════════════════╪═══════════════════════════╪═══════════════════════════╡
│ Boyer-Moore │ 0.009911 sec │ 0.875349 sec │ 0.004115 sec │ 1.530693 sec │
├────────────────────┼───────────────────────────┼───────────────────────────┼───────────────────────────┼───────────────────────────┤
│ Knuth-Morris-Pratt │ 0.009429 sec │ 1.637422 sec │ 0.002970 sec │ 2.141587 sec │
├────────────────────┼───────────────────────────┼───────────────────────────┼───────────────────────────┼───────────────────────────┤
│ Rabin-Karp │ 0.005333 sec │ 3.275581 sec │ 0.002882 sec │ 5.336631 sec │
╘════════════════════╧═══════════════════════════╧═══════════════════════════╧═══════════════════════════╧═══════════════════════════╛
