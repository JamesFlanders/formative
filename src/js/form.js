import {h} from "vue";
import ShortTextField from "@/components/ShortTextField.vue";
import SelectField from "@/components/SelectField.vue";
import LongTextField from "@/components/LongTextField.vue";
import DateField from "@/components/DateField.vue";


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
            name: field.name,
            value: field.defaultValue,
            onInput(event) {
                alert(this[name])
                this[name] = event.target.value
            }
        })
    }
    if (field.type === "longText") {
        vueComponent = h(LongTextField, {
            name: field.name,
            value: field.defaultValue
        })
    }
    if (field.type === "select") {
        vueComponent = h(SelectField, {
            name: field.name,
            options: field.options,
            value: field.defaultValue
        })
    }
    if (field.type === "date") {
        vueComponent = h(DateField, {
            name: field.name,
        })
    }
    return vueComponent
}