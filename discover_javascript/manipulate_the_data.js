var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token ' + process.env.TOKEN
    }
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

var req = https.request(options, function(res){
  combine(res,function(jsonString){
    var data = JSON.parse(jsonString);
    var array = data.items.map(function(project){
      return project.full_name;
    });
    console.log(array.join("\n"));
  });
});
req.end();
