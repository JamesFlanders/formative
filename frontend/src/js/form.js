import {h} from "vue";
import TextField from "@/components/fields/TextField.vue";
import SelectField from "@/components/fields/SelectField.vue";
import TextAreaField from "@/components/fields/TextAreaField.vue";
import DateField from "@/components/fields/DateField.vue";
import NumberField from "@/components/fields/NumberField.vue";


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
    let vueComponent = null

    let required = field.required
    if (required === undefined || required === null) {
        required = false
    }

    if (field.type === "shortText") {
        vueComponent = h(TextField, {
            id: field.id,
            name: field.name,
            subtype: "text",
            required: required,
            value: field.defaultValue,
        })
    }
    if (field.type === "longText") {
        vueComponent = h(TextAreaField, {
            id: field.id,
            name: field.name,
            required: required,
            value: field.defaultValue
        })
    }
    if (field.type === "email") {
        vueComponent = h(TextField, {
            id: field.id,
            name: field.name,
            subtype: "email",
            required: required,
            value: field.defaultValue
        })
    }
    if (field.type === 'number') {
        vueComponent = h(NumberField, {
            id: field.id,
            name: field.name,
            required: required,
            value: field.defaultValue
        })
    }
    if (field.type === "select") {
        vueComponent = h(SelectField, {
            id: field.id,
            name: field.name,
            required: required,
            options: field.options,
            value: field.defaultValue
        })
    }
    if (field.type === "date") {
        vueComponent = h(DateField, {
            id: field.id,
            name: field.name,
            required: required
        })
    }
    return vueComponent
}