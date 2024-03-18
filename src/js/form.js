import {h} from "vue";
import ShortTextField from "@/components/fields/ShortTextField.vue";
import SelectField from "@/components/fields/SelectField.vue";
import LongTextField from "@/components/fields/LongTextField.vue";
import DateField from "@/components/fields/DateField.vue";
import NumberField from "@/components/fields/NumberField.vue";


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
    if (field.type === "shortText") {
        vueComponent = h(ShortTextField, {
            id: field.id,
            name: field.name,
            value: field.defaultValue,
        })
    }
    if (field.type === "longText") {
        vueComponent = h(LongTextField, {
            id: field.id,
            name: field.name,
            value: field.defaultValue
        })
    }
    if (field.type === 'number') {
        vueComponent = h(NumberField, {
            id: field.id,
            name: field.name,
            value: field.defaultValue
        })
    }
    if (field.type === "select") {
        vueComponent = h(SelectField, {
            id: field.id,
            name: field.name,
            options: field.options,
            value: field.defaultValue
        })
    }
    if (field.type === "date") {
        vueComponent = h(DateField, {
            id: field.id,
            name: field.name,
        })
    }
    return vueComponent
}