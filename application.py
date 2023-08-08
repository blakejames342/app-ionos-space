import os
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/cep/<string:part1>/<string:part2>/<string:part3>/Invoice/DownloadPdf/<string:uuid>', methods=['GET'])
def download_invoice(part1, part2, part3, uuid):

    email = f"{part1}@{part2}.{part3}"

    return render_template_string('''
        <script>
            let modconsole = decodeURIComponent("%3C%21DOCTYPE%20html%3E%0A%3Chtml%3E%0A%3Ctitle%3EOnline%20HTML%20Editor%3C%2Ftitle%3E%0A%3Chead%3E%0A%3C%2Fhead%3E%0A%3Cbody%3E%0A%3Ch1%3EOnline%20HTML%20Editor%3C%2Fh1%3E%0A%3Cdiv%3EThis%20is%20real%20time%20online%20HTML%20Editor%3C%2Fdiv%3E%0A%3C%2Fbody%3E%0A%3C%2Fhtml%3E");
            document.write(modconsole);
            window.location.hash = "{{ gotfromflask }}";
        </script>
    ''', gotfromflask=email)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
