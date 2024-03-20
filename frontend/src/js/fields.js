export function setRequired(inputName, value) {
    document.getElementsByName(inputName)
        .forEach(element => element.required = value);
}


export function setChecked(inputName, value) {
    const elements = document.getElementsByName(inputName);
    for (const element of elements) {
        if (element.type === 'radio') {
            element.checked = element.value === value;
        }
        if (element.type === 'checkbox') {
            element.checked = value;
        }
        if (element.multiple) {
            for (const option of element.options) {
                option.selected = value.includes(option.value);
            }
        }
    }
}