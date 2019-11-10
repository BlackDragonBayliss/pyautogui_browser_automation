from flask import Flask, jsonify, request
from automationManager import AutomationManager
app = Flask(__name__)

# def __new__(self):
#     self.automationManager = AutomationManager()

@app.route('/api', methods=['POST'])
def api():
    content = request.get_json()
    return_value = 'pass'
    print(str(content))
    for key, value in content.items():
        if key == 'requestType':
            if value == "quitBrowser":
                print("hit")
                automationManager = AutomationManager()
                automationManager.exitBrowser()
    return "Query received"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=4440)


