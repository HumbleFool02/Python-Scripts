def generate_latex_figures(n, output_file="figures.txt"):
    template = """\\begin{{figure}}[h]
    \centering
    \includegraphics[width=0.5\linewidth]{{{}}}
    \caption{{}}
\\end{{figure}}

"""
    
    with open(output_file, "w") as f:
        for i in range(1, n + 1):
            f.write(template.format(f"Assignment 1 Images/{i}.jpg", i))
    
    print(f"LaTeX figure blocks generated in {output_file}")

# Example usage
n = 23  # Change this to the desired number of repetitions
generate_latex_figures(n)
