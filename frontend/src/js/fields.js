export function setRequired(inputName, value) {
    const elements = document.getElementsByName(inputName);
    for (const element of elements) {
        element.required = value;
    }
}

export function setChecked(inputName, value) {
    const elements = document.getElementsByName(inputName);
    for (const element of elements) {
        element.checked = element.value === value;
    }
}