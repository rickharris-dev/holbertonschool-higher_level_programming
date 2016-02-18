var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token ' + process.env.TOKEN
    }
}

var req = https.request(options, function(res) {
	var body = '';
	res.on('data', function(chunk) {
	   process.stdout.write(chunk);
	    });
});
req.end();
