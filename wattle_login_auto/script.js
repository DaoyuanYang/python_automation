// var webdriver = require("selenium-webdriver"),
// SeleniumServer = require("selenium-webdriver/remote").SeleniumServer;
// alert('Hi')

var username = document.getElementById('username')
var password = document.getElementById('password')
var continue_but = document.getElementsByName('_eventId_proceed')[0]

username.value = "u6547564"
password.value = "dOMEY1999$"

// function sleep(ms) {
//     console.log('Start sleeping')
//     return new Promise(resolve => setTimeout(resolve, ms));
//   }

// await sleep(2)

continue_but.click()

console.log(continue_but)