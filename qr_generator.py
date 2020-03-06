import sys
try:
    import qrcode
except ModuleNotFoundError:
    print('QRCode generation package not installed, please install with the pillow library using:\r\npip install qrcode[pil]')

"""
    To use, install the QR code with the pillow generation library: 
        pip install qrcode[pil]
    
    Then, the script can be used in one of two ways:
        To run from terminal, use the syntax:
            python3 qr_generator.py filename qr_content
        To run with the info loaded into this script:
            Replace the filenames and qr_contents on lines 23 and 24.
            Note: There must be a matching number of filenames and qr_contents.
            Run using the syntax: 
                python3 qr_generator.py
"""

# Setup arguments
command_line_switch = False
if len(sys.argv) > 1:
    filename = sys.argv[1]
    qr_contents = sys.argv[2]
    command_line_switch = True
else:
    filename = ['default', 'test']
    qr_contents = ['default', 'test']

# Generate Code
if command_line_switch:
    code = qrcode.make(qr_contents)
    code.save(f'{filename}.png')
    print(f'Created and saved "{filename}.png" with value: {qr_contents}')
else:
    counter = 0
    for name in filename:
        code = qrcode.make(qr_contents[counter])
        code.save(f'{filename[counter]}.png')
        print(f'Created and saved "{filename[counter]}.png" with value: {qr_contents[counter]}')
        counter += 1
