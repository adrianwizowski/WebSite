Gator(window).on('scroll', doParallax);
var images = [].slice.call(document.querySelectorAll('.layer'));

function getViewportHeight() {
    var a = document.documentElement.clientHeight, b = window.innerHeight;
    return a < b ? b : a;
}

function getViewportScroll() {
    if(typeof window.scrollY != 'undefined') {
        return window.scrollY;
    }
    if(typeof pageYOffset != 'undefined') {
        return pageYOffset;
    }
    var doc = document.documentElement;
    doc = doc.clientHeight ? doc : document.body;
    return doc.scrollTop;
}

function doParallax() {
    var el, elOffset, elHeight,
        offset = getViewportScroll(),
        vHeight = getViewportHeight();

    for(var i in images) {
        el = images[i];
        elOffset = el.offsetTop;
        elHeight = el.offsetHeight;

        if((elOffset > offset + vHeight) || (elOffset + elHeight < offset)) { continue; }

        el.style.backgroundPosition = '50% '+'data-depth'+'px';
    }
}