window.addEventListener(
    'load',
    () => {
        document.body.style.backgroundImage = 'url(/static/img/1.png)'
    }
);

function set_picture(season) {
    var old_pic = document.body.style.backgroundImage;
    console.log(document.body.style.backgroundImage);
    console.log(`url("img/${season}")`);
    var anim = document.body.animate(
        [
          { backgroundImage: `url("/static/img/${season}")` }
        ],
        { duration: 3000, iterations: 1 }
      );
    setTimeout(() => {
        anim.pause();
        console.log('stopped');
        document.body.style.backgroundImage = `url("/static/img/${season}")`;
    }, 2999);
}