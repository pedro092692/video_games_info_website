function add_cover_bg(){
    covers = document.querySelectorAll('.game-cover');
    for(let cover of covers){
        let img_id = cover.getAttribute("id");
        let url = `https://images.igdb.com/igdb/image/upload/t_720p/${img_id}.jpg`;
        cover.style.backgroundImage = "url("+url+")";
    }
}

function search_game(){
    try{
        search_form = document.getElementById('search_form');
        input_search = document.getElementById('search');
        input_search.addEventListener('keyup', ()=>{
            query = input_search.value;
            console.log(query);
            search_form.requestSubmit();
        })
    }catch{
        //pass
    }
}

add_cover_bg();
search_game();