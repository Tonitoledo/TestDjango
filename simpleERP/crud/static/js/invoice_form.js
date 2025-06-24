document.addEventListener('DOMContentLoaded', function() {


    
    

});

function updateUnitPrice(select){
    const selectedProduct = select.options[select.selectedIndex];
    const productId = selectedProduct.value;
    const price = selectedProduct.getAttribute('data-price');
    if (price && productId){ 
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