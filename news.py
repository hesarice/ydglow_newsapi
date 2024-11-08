from flask import Flask, jsonify, request
import ast

app = Flask(__name__)
def find_dict_by_url(file_path,target_url):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    try:
        data = ast.literal_eval(content)
        for item in data:
            if isinstance(item, dict) and item.get('url') == target_url:
                return item

    except (SyntaxError, ValueError) as e:
        print(f"文件解析错误: {e}")
    return None

@app.route('/api/find_dict', methods=['GET'])
def get_dict_by_url():
    target_url = request.args.get('url')
    if not target_url:
        return jsonify({"error": "缺少 url 参数"}), 400
    result = find_dict_by_url('contents.txt', target_url)

    if result:
        print("123")
        return jsonify(result), 200
    else:
        return jsonify({"message": "没有找到包含该 URL 的字典"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5001)  # 使用自定义端口