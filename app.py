from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route('/visit', methods=['GET'])
def visit():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'يرجى إضافة رابط عبر ?url='}), 400

    options = Options()
    options.add_argument("--headless")  # تشغيل بدون واجهة
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service("E:/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        return jsonify({'message': '✅ تم فتح الرابط بنجاح!', 'url': url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
