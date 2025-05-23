# Порівняння алгоритмів сортування: Insertion Sort, Merge Sort та Timsort

## Мета

Емпірично порівняти три алгоритми сортування:

- Insertion Sort (O(n²))
- Merge Sort (O(n log n))
- Вбудований Timsort в Python (гібрид Merge + Insertion)

## Методика

Для порівняння використано модуль `timeit`, що дозволяє точно виміряти час виконання.
Дані генеруються випадково для масивів розміром 100, 500, 1000, 2000 елементів.

## Результати (приклад)

| Розмір масиву | Insertion Sort (с) | Merge Sort (с) | Timsort (с) |
| ------------- | ------------------ | -------------- | ----------- |
| 100           | 0.0012             | 0.0015         | 0.0006      |
| 500           | 0.0257             | 0.0078         | 0.0021      |
| 1000          | 0.0994             | 0.0162         | 0.0045      |
| 2000          | 0.4142             | 0.0369         | 0.0087      |

## Висновки

- **Insertion Sort** значно гальмує при великих обʼємах даних, через квадратичну складність `O(n²)`.
- **Merge Sort** демонструє стабільну ефективність, особливо для великих масивів.
- **Timsort**, що використовується в Python (`sorted` / `.sort()`), обʼєднує переваги обох підходів:
  - Використовує Insertion Sort для малих блоків (де він ефективніший).
  - Merge Sort — для більших.
  - В результаті працює **найшвидше у більшості випадків**.

## Рекомендація

Програмісти зазвичай не реалізовують сортування вручну, оскільки Timsort є:

- Надійним
- Оптимізованим під реальні дані
- Вже реалізованим у Python

Тому **`sorted()` або `.sort()` — найкращий вибір у більшості задач**.
