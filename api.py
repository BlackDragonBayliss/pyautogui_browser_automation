from flask import Flask, jsonify, request
from automationManager import AutomationManager
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    content = request.get_json()
    return_value = 'pass'
    # print(str(content))
    response = "success"
    for key, value in content.items():
        if key == 'requestType':
            if value == "op1":
                print("hit in")
                automationManager = AutomationManager()
#                 # automationManager.exitBrowser()
                automationManager.operationStartCMDClickCenter()
                return "success"
#     print("hit0")
#     content = request.get_json()
#     return_value = 'pass'
#     print(str(content))
#     for key, value in content.items():
#         if key == 'requestType':
#             if value == "op1":
#                 print("hit")
#                 automationManager = AutomationManager()
#                 # automationManager.exitBrowser()
#                 automationManager.operationStartCMDClickCenter()
#                 # automationManager.hold_W(10)
#     return "Query received"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=4460)

