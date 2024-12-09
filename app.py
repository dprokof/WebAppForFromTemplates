from flask import Flask, request, jsonify
from db import load_templates
from utils import validate_field, FIELD_TYPES

app = Flask(__name__)

templates = load_templates()


@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.form.to_dict()

    matched_template = None
    for template in templates:
        if all(field in data and validate_field(data[field], template[field]) for field in template if field != 'name'):
            matched_template = template['name']
            break

    if matched_template:
        return jsonify({"form_name": matched_template})

    field_types = {field: FIELD_TYPES[template[field]] for field in data}
    return jsonify(field_types)


if __name__ == "__main__":
    app.run(debug=True)
