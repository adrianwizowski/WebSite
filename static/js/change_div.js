jQuery(function () {
            var $els = $('div[id^=change]'),
                i = 0,
                len = $els.length;

            $els.slice(1).hide();

            function slider() {
                $els.eq(i).fadeOut(function () {
                    i = (i + 1) % len
                    $els.eq(i).fadeIn();
                })
            }

            var timer = setInterval(slider, 2500);

            $('div[id^=change]').hover(function (ev) {
                clearInterval(timer);
            }, function (ev) {
                timer = setInterval(slider, 2500);
            });
         });
         document.onscroll = function() {
                if (window.innerHeight + window.scrollY > document.body.clientHeight) {
                    document.getElementById('hide').style.display='none';
                    document.getElementById('bottom').style.display='';
                }if (window.innerHeight + window.scrollY < document.body.clientHeight) {
                    document.getElementById('hide').style.display='';
                    document.getElementById('bottom').style.display='none';
                }
            }