from fpdf import FPDF, HTMLMixin

class PDF(FPDF, HTMLMixin):
    pass

pdf = PDF()
pdf.add_page()
pdf.write_html("""
    <table>
        <thead>
            <tr>
                <td><strong>Item</strong></td>
                <td><strong>Price</strong></td>
                <td><strong>Quantity</strong></td>
                <td><strong>Totals</strong></td>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>BS-200</td>
                <td class="text-center">$10.99</td>
                <td class="text-center">1</td>
                <td class="text-right">$10.99</td>
            </tr>
            <tr>
                <td>BS-400</td>
                <td class="text-center">$20.00</td>
                <td class="text-center">3</td>
                <td class="text-right">$60.00</td>
            </tr>
            <tr>
                <td>BS-1000</td>
                <td class="text-center">$600.00</td>
                <td class="text-center">1</td>
                <td class="text-right">$600.00</td>
            </tr>
            <tr>
                <td class="thick-line"></td>
                <td class="thick-line"></td>
                <td class="thick-line text-center"><strong>Subtotal</strong></td>
                <td class="thick-line text-right">$670.99</td>
            </tr>
            <tr>
                <td class="no-line"></td>
                <td class="no-line"></td>
                <td class="no-line text-center"><strong>Shipping</strong></td>
                <td class="no-line text-right">$15</td>
            </tr>
            <tr>
                <td class="no-line"></td>
                <td class="no-line"></td>
                <td class="no-line text-center"><strong>Total</strong></td>
                <td class="no-line text-right">$685.99</td>
            </tr>
        </tbody>
    </table>

""")
pdf.output("html.pdf")
