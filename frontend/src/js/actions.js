import {h, render} from "vue";
import FormResponse from "@/components/FormResponse.vue";

export async function performAction(event) {
    let formElements = event.target.elements;
    let submitButton = document.getElementById("card-submit");
    setButtonToLoading(submitButton);
    let actions = this.form.actions;
    let fields = parseFormElements(formElements);

    let responses = [];
    for (let i = 0; i < actions.length; i++) {
        let action = actions[i];
        if (action.action === 'api') {
            let response = await performApiAction(fields, action);
            responses.push(response);
        }
    }
    renderResponse(responses, 0);
}


export function renderResponse(responses, offset) {
    let aside = document.getElementById("col-right");
    let form = document.getElementById("card-form");

    if (form !== undefined && form !== null) {
        form.remove()
    }

    let currentResponse = responses[offset];
    let formResponseComponent = h(FormResponse, {
        currentResponse: currentResponse,
        offset: offset,
        responses: responses
    })
    render(formResponseComponent, aside);
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


function parseFormElements(formElements) {
    let values = {}
    for (let i = 0; i < formElements.length - 1; i++) {
        let formElement = formElements[i];
        if (formElement.type === "radio" && formElement.checked === false) {
            continue
        }
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
        return response.json().then((data) => {
            return {data: data, status: response.status};
        });
    }).catch((errorResponse) => {
        return errorResponse;
    });
}