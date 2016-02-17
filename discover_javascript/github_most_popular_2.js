var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token ' + process.env.TOKEN
    }
}

    var success = function(stream){

	var print = function(jsonString){
	    console.log(typeof jsonString);
	    console.log(jsonString);
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

	combine(stream,print);
    }
    
var req = https.request(options, success);
req.end();
