window.addEventListener(
    'load',
    () => {
        bigpic.style.backgroundImage = 'url(/static/img/1.png)'
    }
);

function set_picture(season) {
    var old_pic = bigpic.style.backgroundImage;
    console.log(bigpic.style.backgroundImage);
    console.log(`url("img/${season}")`);
    var anim = bigpic.animate(
        [
          { backgroundImage: `url("/static/img/${season}")` }
        ],
        { duration: 3000, iterations: 1 }
      );
    setTimeout(() => {
        anim.pause();
        console.log('stopped');
        bigpic.style.backgroundImage = `url("/static/img/${season}")`;
    }, 2999);
}