function sendMessage(){

    let input=document.getElementById("user-input");
    let message=input.value.trim();

    if(message==="") return;

    let chat=document.getElementById("chat-box");

    chat.innerHTML+=`<div class="user"><b>You:</b><br>${message}</div>`;

    input.value="";

    chat.innerHTML+=`<div class="bot" id="typing">🤖 Typing...</div>`;

    chat.scrollTop=chat.scrollHeight;

    fetch("/chat",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            message:message
        })
    })
    .then(res=>res.json())
    .then(data=>{

        document.getElementById("typing").remove();

        chat.innerHTML+=`
        <div class="bot">
        <b>AI Bot:</b><br>
        ${data.response}
        </div>
        `;

        chat.scrollTop=chat.scrollHeight;

    });

}

document.getElementById("user-input")
.addEventListener("keypress",function(e){

    if(e.key==="Enter")
        sendMessage();

});

function clearChat(){

    document.getElementById("chat-box").innerHTML="";

}