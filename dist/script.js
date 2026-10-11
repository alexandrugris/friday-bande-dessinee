const fill=document.querySelector('#progress-fill');
const update=()=>{const max=document.documentElement.scrollHeight-innerHeight;fill.style.width=`${max>0?(scrollY/max)*100:0}%`};
addEventListener('scroll',update,{passive:true});addEventListener('resize',update);update();
