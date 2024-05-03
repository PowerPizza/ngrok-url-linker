function on_click_save(){
    let url_ = document.querySelector(".entry_url").value;
    if (url_ && url_.length > 1){
        let xml_svr = new XMLHttpRequest();
        xml_svr.open("POST", "/set_url");
        xml_svr.onload = ()=>{
            alert("URL Saved!");
        }
        xml_svr.send(JSON.stringify({"url": url_}))
    }
}