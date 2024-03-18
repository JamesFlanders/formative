export function performAction(event) {
    let formElements = event.target.elements;
    let actions = this.form.actions;
    let fields = parseFormElements(formElements);

    for (let i = 0; i < actions.length; i++) {
        let action = actions[i];
        if (action.action === 'api') {
            let response = performApiAction(fields, action);
        }
    }
}


function parseFormElements(formElements) {
    let values = {}
    for (let i = 0; i < formElements.length; i++) {
        let formElement = formElements[i];
        values[formElement.name] = formElement.value
    }
    return values

}

function parseFieldParameters(fields, value) {
    for (let key in fields) {
        let valueToReplace = '{{' + key + '}}';
        if (typeof value === 'string') {
            value = value.replace(valueToReplace, fields[key]);
        }
        if (typeof value == 'object') {
            for (let key in value) {
                value[key] = value[key].replace(valueToReplace, fields[key]);
            }
        }
    }
    return value
}


function performApiAction(fields, action) {
    let url = parseFieldParameters(fields, action.url);
    if (action.hasOwnProperty("body")) {
        let body = parseFieldParameters(fields, action.body);
        return fetch(url, {method: action.method, body: body}).then(response => {
            return response.json();
        });
    }
    return fetch(url, {method: action.method}).then(response => {
        return response.json();
    });
}