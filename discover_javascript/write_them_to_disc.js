var https = require('https');
var fs = require('fs');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token ' + process.env.TOKEN
    }
}

    var success = function(stream){

	var write = function(jsonString){
	    var file = "/tmp/38";
	    fs.writeFile(file,jsonString);
	    console.log("The file was saved!");
	}

	var combine = function streamToString(stream, cb) {
	    const chunks = [];
	    stream.on('data', (chunk) => {
		    chunks.push(chunk);
		});
	    stream.on('end', () => {
		    cb(chunks.join(''));
		});
	}

	combine(stream,write);
    }
    
var req = https.request(options, success);
req.end();
