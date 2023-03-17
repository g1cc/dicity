// console.log("f");
setInterval(() => {
    // console.log($('.headerHolder').css('height'));
    if ($('.headerHolder').css('height')) {
        $('.content').css("padding-top", $('.headerHolder').css('height'))
    }
    else {
        $('.content').css("padding-top", 0)
    }
}, 100)