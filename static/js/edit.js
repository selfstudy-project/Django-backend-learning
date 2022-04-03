window.onload = function(){
    document.getElementById("preview").innerHTML = marked.parse(document.querySelector("textarea").innerHTML);
    document.getElementById("checknull").style.borderStyle="solid";
    const w=document.body.clientWidth;
    if(w>=700){
        document.getElementById('big').style.display="block";
        var ac = document.getElementsByClassName('top1')
        for(var i=0;i<ac.length;i++){
            ac[i].style.fontSize=(w/60)+"px";
        }
        for(var i=0;i<5;i++){
            document.getElementsByClassName('vertical1')[i].style.fontSize=16+"px";
            document.getElementsByClassName('vertical1')[i].style.height=(w/20)+"px";
        }
    }else if(w>=500){
        document.getElementById('small').style.display="block";
        for(var i=0;i<5;i++){
            document.getElementsByClassName('vertical1')[i].style.fontSize=(w/30)+"px";
            document.getElementsByClassName('vertical1')[i].style.height=(w/40)+"px";
        }
    }else{
        document.getElementById('small').style.display="block";
        for(var i=0;i<5;i++){
            document.getElementsByClassName('vertical1')[i].style.fontSize=(w/20)+"px";
            document.getElementsByClassName('vertical1')[i].style.height=(w/30)+"px";
        }
    }
}
function redirect(a) {
    if(a==1) document.location.href=`index`;
    else if(a==2) window.location.href=`ls`;
    else if(a==3) window.location.href=`pf`;
    else if(a==4) window.location.href=`sf`;
    else if(a==5) window.location.href=`https://tioj.ck.tp.edu.tw/users/gary940610`;
    else if(a==6) window.location.href=`https://codeforces.com/profile/gary940610`;
    else if(a==7) window.location.href=`https://atcoder.jp/users/gary940610`;
    else if(a==8) window.location.href=`https://www.facebook.com/profile.php?id=100008453702626`;
    else if(a==9) window.location.href=`https://forms.gle/eFBd5bsJqCFvNJwj6`;
    else if(a==10) window.location.href=`addpost`
    else if(a==11) window.location.href=`log_in`
    else if(a==12) window.location.href=`account`
}


var input = document.querySelector("textarea")
input.addEventListener("input", update)

function update(e) {
    document.getElementById("preview").innerHTML = marked.parse(e.target.value);
    if(e.target.value=="") {
        document.getElementById("checknull").style.borderStyle="none";
    }
    else document.getElementById("checknull").style.borderStyle="solid";
}

