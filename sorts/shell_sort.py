'''
Shell Sort is an improved version of Insertion Sort, where elements are first sorted at large gaps and 
then progressively reduced until they are sorted at gap = 1.
'''
# Worst case time complexity: O(n^2)
# Best case time complexity: O(n log n)

from .base_sort import BaseSort

class ShellSort(BaseSort):
    complexities = {
        "worst": "O(n²)",
        "average": "O(n log n)",
        "best": "O(n log n)"
    }
    def run(self):
        n = len(self.data)
        gap = n // 2  # Initial gap size

        while gap > 0:
            for i in range(gap, n):
                temp = self.data[i]
                j = i

                while j >= gap and self.data[j - gap] > temp:
                    if not self.running:
                        return

                    self.highlight_bars([j, j - gap], "#e74c3c")  # Highlight comparison
                    self.data[j] = self.data[j - gap]
                    self.draw()
                    self.reset_bars([j, j - gap])

                    j -= gap

                self.data[j] = temp
                self.draw()

            gap //= 2  # Reduce the gap

        self.visualizer.bar_colors = ["#2980b9"] * len(self.data)  # Final sorted color
        self.draw()
