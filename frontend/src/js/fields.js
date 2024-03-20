export function setRequired(inputName, value) {
    let elements = document.getElementsByName(inputName)
    for (let i = 0; i < elements.length; i++) {
        elements[i].required = value
    }
}

export function setChecked(inputName, value) {
    let elements = document.getElementsByName(inputName)
    for (let i = 0; i < elements.length; i++) {
        if (elements[i].value === value) {
            elements[i].checked = value
        }
    }
}