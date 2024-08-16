from fpdf import FPDF
import datetime

def setPdf(Dict):
    pdf = FPDF(orientation='P', unit="mm", format="A4")
    pdf.add_page()

    x = datetime.datetime.now()

    pdf.set_line_width(1)
    pdf.rect(10, 10, 190, 277)

    pdf.set_font(family="Times", size=24, style="B")
    pdf.cell(w=0, h=15, txt="E-ticket", border=0, ln=0, align="L")
    pdf.cell(w=0, h=15, txt="Thawani Flights", border=0, ln=1, align="R")

    pdf.set_font(family="Times", size=12)
    pdf.cell(w=0, h=8, txt="Thawani Booking ID : 23856868100", border=0, ln=1, align="L")
    pdf.cell(w=0, h=8, txt=f"Booked on: {x.strftime("%a")}, {x.strftime("%b")} {x.strftime("%d")}, {x.strftime("%X")}, {x.strftime("%Y")}", border=0, ln=1, align="L")
    pdf.cell(w=0, h=8, txt="Invoice no: PF2024A002904263", border=0, ln=1, align="L")
    pdf.cell(w=0, h=8, txt=f"Invoice Date: {x.strftime("%d")} {x.strftime("%b")}, {x.strftime("%Y")}", border=0, ln=1, align="L")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=95, h=10, txt="Onward Flight", border=1, ln=0, align="L")
    pdf.cell(w=95, h=10, txt="PNR", border=1, ln=1, align="R")
    pdf.cell(w=95, h=10, txt=f"{Dict['Departure City']} to {Dict['Arrival City']}", border=1, ln=0, align="L")
    pdf.cell(w=95, h=10, txt="JPYSRB", border=1, ln=1, align="R")

    # Adding the rest of the information from Dict
    for key, value in Dict.items():
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=95, h=10, txt=str(key), border=1, ln=0, align="L")
        pdf.cell(w=95, h=10, txt=str(value), border=1, ln=1, align="R")

    fare = {
        "Base Fare": "INR 3798",
        "Applicable charges and taxes collected on behalf of airline": "INR 991",
        "Airline Fare": "INR 4789",
        "Seat (collected on behalf of airline)": "INR 130",
        "Convenience Fees (Inclusive of GST)": "INR 325",
        "Instant Discount": "- INR 479",
        "Total Booking Amount": "INR 4765"
    }

    # Adding the Fare & Payment Details section
    # pdf.ln(10)  # Adding some space before the header
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=0, h=12, txt="Fare & Payment Details", border=1, ln=1, align="C")

    for key, value in fare.items():
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=95, h=8, txt=str(key), border=0, ln=0, align="L")
        pdf.cell(w=95, h=8, txt=str(value), border=0, ln=1, align="R")

    pdf.output("output.pdf")