from fpdf import FPDF

# Function to create CS50 shirtificate
def create_shirtificate(name):
    # Create instance of FPDF class
    pdf = FPDF(orientation='P', format='A4')

    # Add a page
    pdf.add_page()

    # Set font for CS50 text
    pdf.set_font("Arial", "", size=48)

    # Title
    pdf.cell(0, 57, "CS50 Shirtificate", align="C")
    pdf.ln(25)

    # Set font for user's name
    pdf.set_font("Arial", size=14)

    # Add shirt image
    pdf.image("shirtificate.png", 10, 70, 190)

    # Overlay user's name on shirt
    pdf.set_font("Arial", size=24)
    pdf.set_text_color(255, 255, 255)  # Set text color to white
    pdf.cell(0, 213, f"{name} - CS50 Grad", align="C")

    # Save the PDF
    pdf.output("shirtificate.pdf")

def main():
    # Prompt user for their name
    name = input("Enter your name: ")
    # Call function to create shirtificate
    create_shirtificate(name)

if __name__ == "__main__":
    main()
