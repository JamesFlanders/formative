import {h, render} from "vue";
import FormResponse from "@/components/FormResponse.vue";

export async function performAction(event) {
    let formElements = event.target.elements;
    let submitButton = document.getElementById("card-submit");
    setButtonToLoading(submitButton);
    let actions = this.form.actions;
    let fields = parseFormElements(formElements);

    let data;
    for (let i = 0; i < actions.length; i++) {
        let action = actions[i];
        if (action.action === 'api') {
            data = await performApiAction(fields, action);
        }
    }
    loadResponse(data);
}

function setButtonToLoading(button) {
    button.setAttribute("disabled", "true");
    button.innerText = "";
    let spanElement = document.createElement('span');
    spanElement.className = 'spinner-border spinner-border-sm';
    spanElement.setAttribute('role', 'status');
    spanElement.setAttribute('aria-hidden', 'true');
    button.appendChild(spanElement);
}

function loadResponse(data) {
    let aside = document.getElementById("col-right");
    let form = document.getElementById("card-form");
    form.remove()
    let formResponseComponent = h(FormResponse, {
        data: data
    })
    render(formResponseComponent, aside)
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
    let body = null;
    let headers = {};

    if (action.hasOwnProperty("body")) {
        body = parseFieldParameters(fields, action.body);
    }

    if (action.hasOwnProperty("headers")) {
        headers = action.headers
    }

    return fetch(url, {
        method: action.method,
        headers: headers,
        body: body
    }).then((response) => {
        return response.json();
    }).catch((errorResponse) => {
        return errorResponse;
    });
}