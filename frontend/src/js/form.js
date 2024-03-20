import {h} from "vue";
import TextField from "@/components/fields/TextField.vue";
import SelectField from "@/components/fields/SelectField.vue";
import TextAreaField from "@/components/fields/TextAreaField.vue";
import DateField from "@/components/fields/DateField.vue";
import NumberField from "@/components/fields/NumberField.vue";
import RadioField from "@/components/fields/RadioField.vue";


export function getFormConfiguration(path) {
    return fetch(path).then((response) => {
        return response.json();
    });
}

export function getFieldComponents(fields) {
    let fieldComponents = []
    for (let field of fields) {
        let vueComponent = addVueElement(field)
        fieldComponents.push(vueComponent)
    }
    return fieldComponents
}

function addVueElement(field) {
    let {id, name, type, required = false, defaultValue, options} = field;
    let vueComponent = null;

    switch (type) {
        case "shortText":
            vueComponent = h(TextField, {id, name, subtype: "text", required, value: defaultValue});
            break;
        case "longText":
            vueComponent = h(TextAreaField, {id, name, required, value: defaultValue});
            break;
        case "email":
            vueComponent = h(TextField, {id, name, subtype: "email", required, value: defaultValue});
            break;
        case "secret":
            vueComponent = h(TextField, {id, name, subtype: "password", required, value: defaultValue});
            break;
        case 'number':
            vueComponent = h(NumberField, {id, name, required, value: defaultValue});
            break;
        case "select":
            vueComponent = h(SelectField, {id, name, required, options, value: defaultValue});
            break;
        case "radio":
            vueComponent = h(RadioField, {id, name, required, options, value: defaultValue});
            break;
        case "date":
            vueComponent = h(DateField, {id, name, required});
            break;
    }
    return vueComponent;
}