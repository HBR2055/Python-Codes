import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger

def merge_pdfs():
    # Open file dialog to select multiple PDF files
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    file_paths = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not file_paths:
        print("No files selected.")
        return

    # Merge the selected PDFs
    merger = PdfMerger()
    for pdf in file_paths:
        merger.append(pdf)

    # Ask user to save merged PDF
    save_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF file", "*.pdf")],
        title="Save Merged PDF As"
    )

    if save_path:
        merger.write(save_path)
        merger.close()
        print(f"Merged PDF saved as: {save_path}")
    else:
        print("Save canceled.")

# Run the merge function
if __name__ == "__main__":
    merge_pdfs()
