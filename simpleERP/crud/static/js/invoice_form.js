document.addEventListener('DOMContentLoaded', function() {
    const addLine = document.getElementById('addLine') 
    addLine.addEventListener('click', add_new_line)



});

function add_new_line(event){
    if (event){
        event.preventDefault()
    }
    const formCopyTarget = document.getElementById('lines-container')
    const emptyForEl = document.getElementById('lineProduct').cloneNode(true) //clone form
    emptyForEl.setAttribute('class', 'line-form mb-3 p-3 border rounded')
    //  add new empty form to our html form 
    formCopyTarget.append(emptyForEl)
}

function updateUnitPrice(select){
    const selectedProduct = select.options[select.selectedIndex];
    const price = selectedProduct.getAttribute('data-price');
    if (price){ 
        const lineForm = select.closest('.line-form');
        const priceInput = lineForm.querySelector('unit-price-input');
        priceInput.value = price;
        calculateLineTotal(lineForm); 
    }
}

function calculateLineTotal(lineForm){
    const quantity = parseFloat(lineForm.querySelector('.quantuty-input').value) || 0;
    const unitPrice = parseFloat(lineForm.querySelector('.unit-price-input').value) || 0;
    const lineTotal = quantity * unitPrice;
    lineForm.querySelector('.line-total').value = lineTotal.toFixed(4);
    updateInvoiceTotal();
}
function updateInvoiceTotal() {
    let total = 0;
    document.querySelectorAll('.line-form').forEach(line => {
        const lineTotal = parseFloat(line.querySelector('.line-total').value) || 0;
        total += lineTotal;
    });
    document.getElementById('invoiceTotal').textContent = total.toFixed(4);
}