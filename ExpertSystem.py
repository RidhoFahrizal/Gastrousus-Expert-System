import tkinter as tk
from tkinter import messagebox

class ExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Identifikasi Infeksi Gastro Usus")

        self.penyakit = [
            "Staphylococcus aureus",
            "Jamur beracun",
            "Salmonellae",
            "Clostridium botulinum",
            "Campylobacter"
        ]

        self.bagansakit = [
            [0, 1, 2, 3, 9],
            [0, 1, 2, 4, 10],
            [0, 1, 2, 5, 6, 9],
            [1, 7, 11],
            [8, 2, 5, 12]
        ]

        self.bagangejala = [
            [1, 2, 4, 5],
            [4, 5, 6],
            [4, 7],
            [4, 8, 9],
            [8, 10],
            [4, 5, 9, 11],
            [4, 8, 11, 12],
            [4, 13],
            [1, 2, 3, 4],
            [14, 15],
            [14, 16],
            [14, 17],
            [18, 19]
        ]

        self.input_vars = [tk.BooleanVar() for _ in range(19)]
        self.sakit = [0.0] * 13
        self.target = [0.0] * 5

        self.build_ui()

    def build_ui(self):
        # Gejala Panel
        gejala_frame = tk.LabelFrame(self.root, text="Gejala", padx=10, pady=10, bg="yellow")
        gejala_frame.grid(row=0, column=0, padx=10, pady=10)

        pertanyaan = [
            "1. Apakah anda sering mengalami buang air besar (>2x)?",
            "2. Apakah anda mengalami berak encer?",
            "3. Apakah anda mengalami berak berdarah?",
            "4. Apakah anda merasa lesu dan tidak bergairah?",
            "5. Apakah anda tidak selera makan?",
            "6. Apakah anda merasa mual dan sering muntah (>1x)?",
            "7. Apakah anda merasa sakit di bagian perut?",
            "8. Apakah tekanan darah anda rendah?",
            "9. Apakah anda merasa pusing?",
            "10. Apakah anda mengalami pingsan?",
            "11. Apakah suhu badan anda tinggi?",
            "12. Apakah anda mengalami luka di bagian tertentu?",
            "13. Apakah anda tidak dapat menggerakkan anggota badan tertentu?",
            "14. Apakah anda pernah memakan sesuatu?",
            "15. Apakah anda memakan daging?",
            "16. Apakah anda memakan jamur?",
            "17. Apakah anda memakan makanan kaleng?",
            "18. Apakah anda membeli susu?",
            "19. Apakah anda meminum susu?"
        ]

        for i, q in enumerate(pertanyaan):
            cb = tk.Checkbutton(gejala_frame, text=q, variable=self.input_vars[i], bg="yellow")
            cb.pack(anchor="w")

        # Output Panel
        output_frame = tk.Frame(self.root)
        output_frame.grid(row=0, column=1, padx=10, pady=10)

        self.threshold_label = tk.Label(output_frame, text="Threshold (%)")
        self.threshold_label.pack()
        self.threshold_entry = tk.Entry(output_frame)
        self.threshold_entry.insert(0, "0")
        self.threshold_entry.pack()

        self.output_text = tk.Text(output_frame, width=40, height=20)
        self.output_text.pack()

        self.result_label = tk.Label(output_frame, text="Anda terkena infeksi :", fg="red")
        self.result_label.pack()

        self.diagnosis_label = tk.Label(output_frame, text="", fg="red", font=("Arial", 12, "bold"))
        self.diagnosis_label.pack()

        self.proses_button = tk.Button(output_frame, text="Proses", command=self.proses)
        self.proses_button.pack(pady=10)

    def proses(self):
        try:
            threshold = float(self.threshold_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Masukkan threshold dalam bentuk angka.")
            return

        input_values = [var.get() for var in self.input_vars]

        for i in range(len(self.bagangejala)):
            tmp = 0.0
            for j in self.bagangejala[i]:
                if input_values[j - 1]:
                    tmp += 100 / len(self.bagangejala[i])
            self.sakit[i] = tmp

        for i in range(len(self.bagansakit)):
            tmp = 0.0
            for j in self.bagansakit[i]:
                tmp += (100 / len(self.bagansakit[i])) * (self.sakit[j] / 100)
            self.target[i] = tmp

        result = ""
        persenmax = 0.0
        imax = 0
        for i, p in enumerate(self.target):
            result += f"{self.penyakit[i]} : {p:.2f} %\n"
            if p > persenmax:
                persenmax = p
                imax = i

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)

        if persenmax >= threshold:
            self.diagnosis_label.config(text=self.penyakit[imax])
        else:
            self.diagnosis_label.config(text="none")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpertSystem(root)
    root.mainloop()
