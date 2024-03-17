export function performAction(event) {
    let form = event.target.elements;
    for (let i = 0; i < form.length; i++) {
        alert(form[i].value)
    }
}

function performApiAction(form) {

}