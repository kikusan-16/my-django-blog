$(function(){
    const content = document.querySelector('.page_content');
    h = content.clientHeight
    w = content.clientWidth
    const canvas = document.querySelector('#canvas');

    canvas.setAttribute('height', h+30)
    canvas.setAttribute('width', w)
    const ctx = canvas.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(0, h+30);
    ctx.lineTo(0, h*0.8);
    ctx.lineTo(w, h*0.2)
    ctx.lineTo(w, 0);
    ctx.lineTo(w, h+30);
    ctx.closePath();
    ctx.fillStyle = '#17a2b8';
    ctx.fill();
});