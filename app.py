from flask import Flask, render_template, request, send_file
import qrcode

app = Flask(__name__)

# Root route to display form
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate QR code
@app.route('/generate', methods=['POST'])
def generate_qr():
    url = request.form['url']
    
    # Generate QR code
    img = qrcode.make(url)
    img_path = 'static/qr_code.png'
    img.save(img_path)
    
    return render_template('generate.html', img_path=img_path, url=url)

# Route to download QR code image
@app.route('/download')
def download_qr():
    path = 'static/qr_code.png'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
