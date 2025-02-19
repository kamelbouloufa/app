from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)

@app.route('/visit', methods=['GET'])
def visit():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'يرجى إضافة رابط عبر ?url='}), 400

    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")  # يحاكي شاشة كاملة

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(5)  # انتظار تحميل الصفحة (يمكن تعديل المدة حسب الحاجة)

        return jsonify({'message': '✅ تم فتح الرابط بنجاح!', 'url': url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
