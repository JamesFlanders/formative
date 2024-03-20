export function setRequired(inputName, value) {
    const elements = document.getElementsByName(inputName);
    for (const element of elements) {
        element.required = value;
    }
}

export function setChecked(inputName, value) {
    const elements = document.getElementsByName(inputName);
    for (const element of elements) {
        if (element.type === 'radio') {
            element.checked = element.value === value;
        }
        if (element.multiple) {
            for (const option of element.options) {
                option.selected = value.includes(option.value);
            }
        }
    }
}