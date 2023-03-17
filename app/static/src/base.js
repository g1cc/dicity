// console.log("f");
setInterval(() => {
    console.log($('.headerHolder').css('height'));
    if ($('.headerHolder').css('height')) {
        $('#padding').css("padding-top", $('.headerHolder').css('height'))
    }
    else {
        $('#padding').css("padding-top", 0)
    }
}, 100)