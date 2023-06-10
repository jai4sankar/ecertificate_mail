import xlrd
import smtplib
import os
import sys
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Add participant name to certificate
def make_certi(name):
    if(type=='P'):
        img = Image.open("certificate/E-Cetificate.jpg")
    elif(type=='L'):
        img = Image.open("certificate/spss.jpg")
    draw = ImageDraw.Draw(img)

    # Load font
    font = ImageFont.truetype("font/times.ttf", 80)
    font_id = ImageFont.truetype("font/times.ttf", 40)


    if name == -1:
        return -1
    else:
        if(type=='P'):
        # Insert text into image template
            width, height = (2400, 3100)
            #text='Dilipsasdrgbvhyujrdftgasdrasfs'
            if(len(name)>20):
                font = ImageFont.truetype("font/times.ttf", 60)
            if(len(name)>28):
                font = ImageFont.truetype("font/times.ttf", 50)
            
            font_width, font_height = font.getsize(name)
            new_width = (width - font_width) / 2
            new_height = (height - font_height) / 2
            
            draw.text( (new_width, new_height), name, (0,0,0), font=font ) #draw.text((x, y), message, fill=color, font=font)
            draw.text( (500,300), certificate, (0,0,0), font=font_id )
        elif(type=='L'):
            width, height = (3508, 2600)
           # text='Dilip'
            font_width, font_height = font.getsize(name)
            new_width = (width - font_width) / 2
            new_height = (height - font_height) / 2
            
            draw.text( (new_width, new_height), name, (0,0,0), font=font ) #draw.text((x, y), message, fill=color, font=font)
            draw.text( (250,200), certificate, (0,0,0), font=font_id )
        #img.show() 

        if not os.path.exists( 'certificates' ) :
            os.makedirs( 'certificates' )

        # Save as a PDF
      #  rgb = Image.new('RGB', img.size, (0, 0, 0))  # white background
      #  rgb.paste(img, mask=img.split()[0])               # paste using alpha channel as mask
        
        img.save( 'certificates/'+str(name)+'.pdf', "PDF", resolution=100.0, transparency=10)
        return 'certificates/'+str(name)+'.pdf'

# Email the certificate as an attachment
def email_certi( filename, receiver, name ):
    username = ""
    password = ""
    sender = username + '@gmail.com'
    cc = username

    msg = MIMEMultipart()
    msg['Subject'] = 'E-Certificate - Inspiress'
    msg['From'] = username+'@gmail.com'
    msg['Reply-to'] = username
    msg['To'] = receiver
    msg['Cc'] = username

    # That is what u see if dont have an email reader:
    msg.preamble = 'Multipart massage.\n'

    # cc    
    
    # Body
    body = "Hello {},\n\nCongratulations for completing the course and receiving your certificate from Inspiress.\n\nPlease find the attachment for your E-Certificate.\n\n Regards,\nInspire Solutions".format(name)
    part = MIMEText(body)
    msg.attach( part )

    # Attachment
    part = MIMEApplication(open(filename,"rb").read())
    part.add_header('Content-Disposition', 'attachment', filename = os.path.basename(filename))
    msg.attach( part )

    # Login
    server = smtplib.SMTP( 'smtp.gmail.com:587' )
    server.starttls()
    server.login( username, password )

    # Send the email
    server.sendmail( msg['From'], (msg['To'],cc), msg.as_string() )

if __name__ == "__main__":
    error_list = []
    error_count = 0

    os.chdir(os.path.dirname(os.path.abspath((sys.argv[0]))))

    # Read data from an excel sheet from row 2
    Book = xlrd.open_workbook("data/data.xlsx")
    WorkSheet = Book.sheet_by_name('Sheet1')
    
    num_row = WorkSheet.nrows - 1
    row = 0

    while row < num_row:
        row += 1
        
        name = WorkSheet.cell_value( row, 2 ).upper()
        email = WorkSheet.cell_value( row, 1 )
        certificate = WorkSheet.cell_value( row, 3 )
        type = WorkSheet.cell_value( row, 4 )
        
        # Make certificate and check if it was successful
        filename = make_certi(name)
        
        # Successfully made certificate
        if filename != -1:
           # email_certi( filename, email, name)
            print("Sent to ", name)
            os.remove('certificates/'+str(name)+'.pdf')
        # Add to error list
        else:
            error_list.append( name )
            error_count += 1

    # Print all failed IDs
    print(str(error_count)," Errors- List:", ','.join(error_list))
