window.onload = function(){
    const w=document.body.clientWidth;
    if(w>=700){
        document.getElementById('big').style.display="block";
        for(var i=0;i<4;i++){
            document.getElementsByClassName('top1')[i].style.fontSize=(w/45)+"px";
        }
        for(var i=0;i<5;i++){
            document.getElementsByClassName('vertical1')[i].style.fontSize=(w/50)+"px";
            document.getElementsByClassName('cc')[i].style.height=(w/60)+"px";
        }
    }else if(w>=500){
        document.getElementById('small').style.display="block";
        for(var i=0;i<5;i++){
            document.getElementsByClassName('vertical1')[i].style.fontSize=(w/30)+"px";
            document.getElementsByClassName('cc')[i].style.height=(w/40)+"px";
        }
    }else{
        document.getElementById('small').style.display="block";
        for(var i=0;i<5;i++){
            document.getElementsByClassName('vertical1')[i].style.fontSize=(w/20)+"px";
            document.getElementsByClassName('cc')[i].style.height=(w/30)+"px";
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
}

