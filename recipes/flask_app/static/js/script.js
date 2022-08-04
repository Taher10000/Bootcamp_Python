

var searchForm = document.getElementById('searchForm')
searchForm.addEventListener("submit",function(e){
    
    e.preventDefault();
    var resultsDiv = document.querySelector('#results')
    resultsDiv.innerHTML = ''
    // var searchForm = document.getElementById('searchForm')
    var form = new FormData(searchForm);
    fetch('/api/recipes/all',{method:'POST',body:form})
        .then(res => res.json() )
        .then( data => {
            console.log(data);
            console.log(data.products);
        
            for (const item of data.products) {
                resultsDiv.innerHTML+= `
                <div class="d-flex">
                <img src="${item.image}" alt="">
                <h3>${item.title}</h3>
                </div>
                `
                
            }
        } )

        
})
