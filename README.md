| Algorithm          | Real Substring (Text 1) | Fake Substring (Text 1) | Real Substring (Text 2) | Fake Substring (Text 2) |
| ------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| Boyer-Moore        | 0.003366 sec            | 0.244850 sec            | 0.001180 sec            | 0.335931 sec            |
| Knuth-Morris-Pratt | 0.002682 sec            | 1.373672 sec            | 0.003583 sec            | 2.684720 sec            |
| Rabin-Karp         | 0.008703 sec            | 4.899921 sec            | 0.007822 sec            | 5.991032 sec            |

Загальні висновки:

Boyer-Moore:

- Реальний підрядок (середнє): 0.002273 сек
- Фейковий підрядок (середнє): 0.290391 сек

Knuth-Morris-Pratt:

- Реальний підрядок (середнє): 0.003132 сек
- Фейковий підрядок (середнє): 2.029196 сек

Rabin-Karp:

- Реальний підрядок (середнє): 0.008262 сек
- Фейковий підрядок (середнє): 5.445977 сек

В середньому Boyer-Moore є швидшим за інші, а Rabin-Karp найповільніший.
