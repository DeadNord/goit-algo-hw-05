import timeit
from tabulate import tabulate
import matplotlib.pyplot as plt


def read_text_file(file_path):
    with open(file_path, "rb") as file:
        return file.read().decode("utf-8", "replace")


def plot_results(algorithms, real_times, fake_times, title):
    if real_times or fake_times:
        plt.figure(figsize=(10, 6))
        x = range(len(algorithms))

        if real_times:
            plt.bar(x, real_times, width=0.4, label="Real Substring", align="center")
        if fake_times:
            # Зміщення x для фейкових даних
            x_fake = [i + 0.4 for i in x]
            plt.bar(
                x_fake, fake_times, width=0.4, label="Fake Substring", align="center"
            )

        plt.xlabel("Algorithms")
        plt.ylabel("Execution Time (seconds)")
        plt.title(title)
        plt.xticks(x, algorithms)
        plt.legend()
        plt.show()


def main(text_file1, text_file2):
    # Зчитати зміст текстових файлів
    text1 = read_text_file(text_file1)
    text2 = read_text_file(text_file2)

    # Згенерувати реальний патерн, взятий з першого тексту
    real_pattern_text1 = text1[200:205]
    real_pattern_text2 = text2[300:305]

    # Згенерувати вигаданий патерн
    fake_pattern = "abcdefgh"

    # Ініціалізувати списки для збереження часів виконання
    algorithms = ["Boyer_Moore", "Knuth_Morris_Pratt", "Rabin_Karp"]
    real_times_text1 = []
    fake_times_text1 = []
    real_times_text2 = []
    fake_times_text2 = []

    # Тестування алгоритмів
    for algorithm in algorithms:
        try:
            module = __import__(algorithm.lower())  # імпорт модуля з алгоритмом
            algorithm_func = getattr(
                module, algorithm.lower()
            )  # отримання функції з модуля

        except (ImportError, AttributeError):
            print(f"Warning: Algorithm '{algorithm}' not found.")
            continue

        real_time_text1 = timeit.timeit(
            lambda: algorithm_func(text1, real_pattern_text1), number=1000
        )
        fake_time_text1 = timeit.timeit(
            lambda: algorithm_func(text1, fake_pattern), number=1000
        )
        real_time_text2 = timeit.timeit(
            lambda: algorithm_func(text2, real_pattern_text2), number=1000
        )
        fake_time_text2 = timeit.timeit(
            lambda: algorithm_func(text2, fake_pattern), number=1000
        )

        real_times_text1.append(real_time_text1)
        fake_times_text1.append(fake_time_text1)
        real_times_text2.append(real_time_text2)
        fake_times_text2.append(fake_time_text2)

    # Виведення результатів у вигляді таблички
    table = [
        [
            "Algorithm",
            "Real Substring (Text 1)",
            "Fake Substring (Text 1)",
            "Real Substring (Text 2)",
            "Fake Substring (Text 2)",
        ],
        [
            "Boyer-Moore",
            f"{real_times_text1[0]:.6f} sec" if real_times_text1 else "",
            f"{fake_times_text1[0]:.6f} sec" if fake_times_text1 else "",
            f"{real_times_text2[0]:.6f} sec" if real_times_text2 else "",
            f"{fake_times_text2[0]:.6f} sec" if fake_times_text2 else "",
        ],
        [
            "Knuth-Morris-Pratt",
            f"{real_times_text1[1]:.6f} sec" if real_times_text1 else "",
            f"{fake_times_text1[1]:.6f} sec" if fake_times_text1 else "",
            f"{real_times_text2[1]:.6f} sec" if real_times_text2 else "",
            f"{fake_times_text2[1]:.6f} sec" if fake_times_text2 else "",
        ],
        [
            "Rabin-Karp",
            f"{real_times_text1[2]:.6f} sec" if real_times_text1 else "",
            f"{fake_times_text1[2]:.6f} sec" if fake_times_text1 else "",
            f"{real_times_text2[2]:.6f} sec" if real_times_text2 else "",
            f"{fake_times_text2[2]:.6f} sec" if fake_times_text2 else "",
        ],
    ]

    # Вивід таблички
    print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))

    # Вивід графіка
    plot_results(
        algorithms,
        real_times_text1,
        fake_times_text1,
        title="Algorithm Performance (Text 1)",
    )
    plot_results(
        algorithms,
        real_times_text2,
        fake_times_text2,
        title="Algorithm Performance (Text 2)",
    )


if __name__ == "__main__":
    main("./task_3/article_1.txt", "./task_3/article_2.txt")
    # plt.show()
