import tkinter as tk
import os
import unittest

# ---------------- Calculator Logic ----------------
def calculate(expression: str) -> str:
    """Evaluate the calculator expression and return result as string"""
    try:
        result = str(eval(expression.replace("×", "*").replace("÷", "/")))
        return result
    except:
        return "Error"

# ---------------- GUI Code ----------------
def run_gui():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("320x480")
    root.config(bg="#0E001E")

    entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.FLAT,
                     justify="right", bg="#48395D", fg="#FEFEFE", insertbackground="white")
    entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

    buttons = [
        ["ON", "OFF", "M+", "MC"],
        ["MR", "C", "CE", "%"],
        ["7", "8", "9", "÷"],
        ["4", "5", "6", "×"],
        ["1", "2", "3", "-"],
        ["00", "0", ".", "+"],
        ["", "", "", "="]
    ]

    button_colors = {
        "=": "#563187", "+": "#563187", "-": "#563187", "×": "#563187", "÷": "#563187",
        "ON": "#9F82A0", "OFF": "#9F82A0", "CE": "#310374", "%": "#563187"
    }

    def click(event):
        btn_text = event.widget["text"]
        if btn_text == "=":
            entry.delete(0, tk.END)
            entry.insert(tk.END, calculate(entry.get()))
        elif btn_text == "C":
            entry.delete(0, tk.END)
        elif btn_text == "CE":
            entry.delete(len(entry.get()) - 1)
        else:
            entry.insert(tk.END, btn_text)

    for row in buttons:
        frame = tk.Frame(root, bg="#0E001E")
        frame.pack(expand=True, fill="both", padx=5, pady=2)
        for btext in row:
            color = button_colors.get(btext, "#310374")
            btn = tk.Button(frame, text=btext, font=("Arial", 16, "bold"),
                            bg=color, fg="white", relief="flat", bd=3,
                            activebackground="#06000D", activeforeground="white")
            btn.pack(side=tk.LEFT, expand=True, fill="both", padx=3, pady=3)
            btn.bind("<Button-1>", click)

    root.mainloop()

# ---------------- Test Cases ----------------
class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate("2+3"), "5")
        print("Addition test passed!")

    def test_subtraction(self):
        self.assertEqual(calculate("10-4"), "6")
        print("Subtraction test passed!")

    def test_multiplication(self):
        self.assertEqual(calculate("3×5"), "15")
        print("Multiplication test passed!")

    def test_division(self):
        self.assertEqual(calculate("20÷4"), "5.0")
        print("Division test passed!")

    def test_error(self):
        self.assertEqual(calculate("10/0"), "Error")
        print("Error handling test passed!")

# ---------------- Main Execution ----------------
if __name__ == "__main__":
    if os.environ.get('JENKINS_HOME'):
        print("Running in Jenkins – executing tests")
        unittest.main()
    else:
        run_gui()
