var ft = $('.number img').get()[0];
var fs = $('.number img').get()[1];
var stop = 0;
var down = false;
var up = false;
var floor = [];
var run = false;
var opendoor = false;
var time = 0;
var ip = '36.228.196.251:5000'

$.fn.open = function () {
    setTimeout(function () {
        $("#door_left").animate2({
            transform: "translate(-65%, 0%)",
        }, 2000)
        $("#door_right").animate2({
            transform: "translate(65%, 0%)",
        }, 2000)
        $("#door_left").delay(2000).animate2({
            transform: "translate(0%, 0%)",
        }, 2000)
        $("#door_right").delay(2000).animate2({
            transform: "translate(0%, 0%)",
        }, 2000)
    }, 1800);
};
$("#button2").click(function () {
    $("#door_left").stop(true, false).animate2({
        transform: "translate(-65%, 0%)",
    }, 2000)
    $("#door_right").stop(true, false).animate2({
        transform: "translate(65%, 0%)",
    }, 2000)
});
$("#button3").click(function () {
    $("#door_left").stop(true, false).animate2({
        transform: "translate(0%, 0%)",
    }, 2000)
    $("#door_right").stop(true, false).animate2({
        transform: "translate(0%, 0%)",
    }, 2000)
});

$('#button6').click(function () {
    timerInterval = setInterval(async () => {
        console.log(floor)
        const res = await fetch(`http://${ip}/get_i`, {
            method: "POST",
        })
        const data = await res.json()
        const i = data.i;
        time = data.open ? 2000 : time
        time = data.close ? 0 : time
        console.log(i)
        console.log(`open:${data.open},close:${data.open}`)
        if (run && !opendoor) {
            elerun()
        }
        if (!run) {
            floor = []
            down = ft.id > i ? true : false
            up = ft.id < i ? true : false
            run = down || up ? true : false
            if (run) {
                $('.sign img').attr("src", '/images/' + (down ? 'down.png' : 'up.png'));
                floor.push(i)
                $(".waiting").html(`等候樓層： ${floor}`);
                setTimeout(() => {
                    $('.sign').css('opacity', '0.8');
                }, 50)
            }
            if (time == 2000 && !opendoor) {
                opendoor = true;
                await door_new();
                opendoor = false;
            };
        } else {
            if (((ft.id > i && down) || (ft.id < i && up)) && !floor.some(n => i == n)) {
                floor.push(i)
                floor.sort((i, b) => { return up ? (i - b) : (b - i) })
                $(".waiting").html(`等候樓層： ${floor}`);
            }
        }
    }, 1000);
});


async function elerun() {
    if (run) {
        ft.id = parseInt(ft.id, 10) + (down ? -1 : 1)
        fs.id = parseInt(fs.id, 10) + (down ? -1 : 1)
        console.log(fs.id)
        $('.number img').attr("src", '/images/' + fs.id + '.png');
        if (fs.id == floor[0]) {
            floor.shift();
            $(".waiting").html(`等候樓層： ${floor}`);
            if (!floor.length) {
                $('.sign').css('opacity', '0');
                $(".waiting").html('等候樓層：');
                fetch(`http://${ip}/change`, {
                    method: "POST",
                    headers: {
                        "Content-type": "application/json",
                    },
                    body: JSON.stringify({ "text": fs.id }),
                }).then(() => run = false)
            }
            opendoor = true;
            await door_new();
            opendoor = false;
        }
    }
}



function first_open() {
    return new Promise(res => {
        time = 2000;
        setTimeout(function () {
            $("#door_left").animate2({
                transform: "translate(-65%, 0%)",
            }, 2000)
            $("#door_right").animate2({
                transform: "translate(65%, 0%)",
            }, 2000)
        }, 1800);
        setTimeout(() => res(), 3800);
    })
}

async function door_new() {
    await first_open();
    return new Promise(res => {
        let time_interval = setInterval(() => {
            time -= 100;
            if (time <= 0) {
                clearInterval(time_interval);
                $("#door_left").animate2({
                    transform: "translate(0%, 0%)",
                }, 2000);
                $("#door_right").animate2({
                    transform: "translate(0%, 0%)",
                }, 2000);
                setTimeout(() => res(), 2500);
            };
        }, 100);
    })
}



$.fn.animate2 = function (properties, duration, ease) {
    ease = ease || 'ease';
    var $this = this;
    var cssOrig = { transition: $this.css('transition') };
    return $this.queue(next => {
        properties['transition'] = 'all ' + duration + 'ms ' + ease;
        $this.css(properties);
        setTimeout(function () {
            $this.css(cssOrig);
            next();
        }, duration);
    });
};

$(document).ready(async function () {
    const res = await fetch(`http://${ip}/get_i`, {
        method: "POST",
    })
    const data = await res.json()
    const a = data.i;
    ft.id = a;
    fs.id = a;
    $('.number img').attr("src", '/images/' + fs.id + '.png');
});
