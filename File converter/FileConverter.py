import pandas as pd
from fpdf import FPDF


def txt_to_pdf(txt_file, pdf_file):
    pdf = FPDF() # Creating a PDF document
    pdf.set_auto_page_break(auto=True, margin=15) # Automatic line wrapping
    pdf.add_page() # Adding a page
    pdf.set_font("Arial", size=12) # Setting the font and size

    with open(txt_file, "r", encoding="utf-8") as file:
        for line in file:
            pdf.cell(200, 10, txt=line.strip(), ln=True) # Adding each line to the PDF

    pdf.output(pdf_file) # Saving the PDF file
    print(f"File saved as {pdf_file}")

def csv_to_xlsx(csv_file, xlsx_file):
    df = pd.read_csv(csv_file) # Uploading the CSV file to the DataFrame (table)
    df.to_excel(xlsx_file, index=False) # Save in Excel without indexes
    print(f"File saved as {xlsx_file}")

def main():
    print("Select conversion format: ")
    print("1 - TXT в PDF")
    print("2 - CSV в XLSX")

    choice = input("Enter the operation number: ")

    if choice == "1":
        txt_to_pdf("D:\SB Python\Project python\File Converter\example.txt", "D:\SB Python\Project python\File Converter\output.pdf")
    elif choice == "2":
        csv_to_xlsx("D:\SB Python\Project python\File Converter\example.csv", "D:\SB Python\Project python\File Converter\output.xlsx")
    else:
        print("Wrong select")

if __name__ == "__main__":
    main()