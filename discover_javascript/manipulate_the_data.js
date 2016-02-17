var https = require('https');
var fs = require('fs');
var map = Array.prototype.map;

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token ' + process.env.TOKEN
    }
}

    var success = function(stream){

	var log = function(element){
	    var name = element['full_name'];
	    return name;
	}
	    
	var parse = function(jsonString){
	    var map = Array.prototype.map;
	    var data = JSON.parse(jsonString);
	    var array = map.call(data['items'],log);
	    array = array.join("\n");
	    console.log(array);
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

	combine(stream,parse);
    }
    
var req = https.request(options, success);
req.end();
