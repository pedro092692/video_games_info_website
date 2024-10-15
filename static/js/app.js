function add_cover_bg(){
    covers = document.querySelectorAll('.game-cover');
    for(let cover of covers){
        let img_id = cover.getAttribute("id");
        let url = `https://images.igdb.com/igdb/image/upload/t_720p/${img_id}.jpg`;
        cover.style.backgroundImage = "url("+url+")";
    }
}

add_cover_bg();