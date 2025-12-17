# main_gui.py
import tkinter as tk
import random
import math
import time

from algorithm1 import run_naive_mst
from algorithm2 import run_optimized_mst


# =========================(GUI)==============================
class MSTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project: MST Algorithms Comparison")
        self.root.geometry("1200x650")

        self.control_frame = tk.Frame(root, bg="#f0f0f0", pady=15, padx=10)
        self.control_frame.pack(side=tk.TOP, fill=tk.X)

        self.btn_generate = tk.Button(self.control_frame, text="1. Generate Buildings", 
                                    command=self.generate_buildings, 
                                    bg="#3498db", fg="white", font=("Arial", 10, "bold"))
        self.btn_generate.pack(side=tk.LEFT, padx=10)

        self.btn_naive = tk.Button(self.control_frame, text="2. Run Naive (DFS)", 
                                command=self.solve_naive, 
                                bg="#e74c3c", fg="white", font=("Arial", 10, "bold"))
        self.btn_naive.pack(side=tk.LEFT, padx=10)

        self.btn_opt = tk.Button(self.control_frame, text="3. Run Optimized (Union-Find)", 
                                command=self.solve_optimized, 
                                bg="#2ecc71", fg="white", font=("Arial", 10, "bold"))
        self.btn_opt.pack(side=tk.LEFT, padx=10)

        self.info_frame = tk.Frame(root, bg="#ddd", pady=5)
        self.info_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.lbl_status = tk.Label(self.info_frame, text="Status: Ready", bg="#ddd", width=30, anchor="w")
        self.lbl_status.pack(side=tk.LEFT, padx=20)
        
        self.lbl_time = tk.Label(self.info_frame, text="Time: 0.000s", font=("Arial", 11, "bold"), bg="#ddd", fg="blue")
        self.lbl_time.pack(side=tk.RIGHT, padx=20)

        self.lbl_cost = tk.Label(self.info_frame, text="Cost: 0", font=("Arial", 11, "bold"), bg="#ddd")
        self.lbl_cost.pack(side=tk.RIGHT, padx=20)

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.buildings = [] 
        self.num_buildings = 700 # Num of Duildings


# =========================(Functions)==============================
    def generate_buildings(self):
        self.canvas.delete("all") 
        self.buildings = []
        
        self.lbl_cost.config(text="Cost: 0")
        self.lbl_time.config(text="Time: 0.000s")
        self.lbl_status.config(text="Status: Buildings Generated")

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if width < 100: width = 800
        if height < 100: height = 600

        for i in range(self.num_buildings):
            x = random.randint(50, width - 50)
            y = random.randint(50, height - 50)
            self.buildings.append((x, y))
            
            r = 5
            self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="#34495e", outline="")
            self.canvas.create_text(x, y-10, text=str(i), fill="#95a5a6", font=("Arial", 7))

    def prepare_edges(self):
        edges = []
        n = len(self.buildings)
        for i in range(n):
            for j in range(i + 1, n):
                # (Euclidean Distance)
                x1, y1 = self.buildings[i]
                x2, y2 = self.buildings[j]
                dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
                edges.append((i, j, dist))
        return edges, n

    def draw_results(self, mst_edges, cost, exec_time, method_name, color):
        self.canvas.delete("cable") 
        
        for u, v, w in mst_edges:
            x1, y1 = self.buildings[u]
            x2, y2 = self.buildings[v]
            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2, tags="cable")
        
        self.canvas.tag_lower("cable") 
        
        self.lbl_cost.config(text=f"Cost: {int(cost)}")
        self.lbl_time.config(text=f"Time: {exec_time:.6f}s")
        self.lbl_status.config(text=f"Status: Solved by {method_name}")

# =========================(Naive)==============================
    def solve_naive(self):
        if not self.buildings: return
        self.lbl_status.config(text="Running Naive (DFS)... Please Wait")
        self.root.update() 
        
        edges, n = self.prepare_edges()
        
        start_time = time.time()
        mst_edges, cost = run_naive_mst(n, edges)
        end_time = time.time()
        
        self.draw_results(mst_edges, cost, end_time - start_time, "Naive (DFS)", "#e74c3c")

# =========================(Optimized)==============================
    def solve_optimized(self):
        if not self.buildings: return
        
        edges, n = self.prepare_edges()
        
        start_time = time.time()
        mst_edges, cost = run_optimized_mst(n, edges)
        end_time = time.time()
        
        self.draw_results(mst_edges, cost, end_time - start_time, "Optimized (Union-Find)", "#2ecc71")

if __name__ == "__main__":
    root = tk.Tk()
    app = MSTApp(root)
    root.after(500, app.generate_buildings)
    root.mainloop()



