import qrcode

# take upi id as a input
upi_id=input("Enter your UPI ID: ")
# Upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
# Pa=the upi id we will do payment on it
# pn=recipient name
# am=amount 
# cu=currency
# tn=payment message 

Phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
Googlepay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
Paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

Phonepe_qr=qrcode.make(Phonepe_url)
paytm_qr=qrcode.make(Paytm_url)
googlepay_qr=qrcode.make(Googlepay_url)

# save the  Qr code
Phonepe_qr.save('Phonepe_qr.png')
paytm_qr.save('Phonepe_qr.png')
googlepay_qr.save('Phonepe_qr.png')

# Display the Qr code
Phonepe_qr.show()
googlepay_qr.show()
paytm_qr.show()