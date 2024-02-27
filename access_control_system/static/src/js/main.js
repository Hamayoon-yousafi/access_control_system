const resultDIV = document.getElementById('result-div');
const barcodeInput = document.getElementById('barcode-search-input');

function formSubmission(form, event) {
    event.preventDefault()
    validateBarcode()
}

async function validateBarcode(){
    barcode = barcodeInput.value;
    if(barcode){
        const response = await fetch(`/check-barcodes/validate?barcode=${barcodeInput.value}`);
        try {
            if (!response.ok) {
                throw new Error(`Failed to fetch data. Status: ${response.status}`);
            }
            data = await response.json()
            if (data.employee) {
                renderBarcodeApproval(data.employee);
            } else {
                renderBarcodeDenial()
            }
            setTimeout(function() { clearSearch(); }, 5000);
        } catch (error) {
            console.error('Fetch error:', error);
        }
    }
}

function renderBarcodeApproval(data) {
    resultDIV.innerHTML = `
    <div class="alert alert-success" role="alert">
        Authorized
    </div>
    <div class="details">
        <h5>Name: ${data.name}</h5>
        <h5>Reference: ${data.reference}</h5>
        <h5>ID Number: ${data.employee_id_number}</h5>
    </div>
    `
}

function renderBarcodeDenial(){
    resultDIV.innerHTML = `
    <div class="alert alert-danger" role="alert">
        Unauthorized
    </div>
    `
}

function clearSearch(){
    barcodeInput.value = ''
    resultDIV.innerHTML = ''
}