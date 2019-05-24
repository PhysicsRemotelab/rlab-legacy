function getRemainingTime(updated) {
    var start = new Date(updated)
    start = new Date(start.getTime() + (start.getTimezoneOffset() * 60 * 1000))
    var end = new Date(start.getTime() + (1 * 60 * 1000))
    var now = new Date()
    var time = end - now
    if(time < 0) {
        time = 0
    }
    return time
}

export { getRemainingTime }
