var https = require('https');
var fs = require('fs');
const map = Array.prototype.map;
const final_obj = [];
process.env['COUNT'] = 0;
process.env['REQUESTS'] = 1;

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token ' + process.env.TOKEN
    }
}

    var success = function(stream){

	var log = function(array,key){
	    var item = {};
	    try {
		item[key] = array[key];
	    }
	    catch(err){
		item[key] = '';
	    }
            return item;
	}

	var waiting = function(){
	    if(process.env.REQUESTS == process.env.COUNT){
		var final_string = JSON.stringify(final_obj) + '\n';
		fs.writeFile('/tmp/38',final_string);
		console.log("The file was saved!");
	    }
	}

	var location = function(array){
	    var repo = array.full_name;
	    var users = repo.split('/');
	    var user = users[0];
	    var user_options = {
	    	hostname: 'api.github.com',
	    	path: '/users/' + user + '?q=language:javascript',
	    	headers: {
	    	    'User-Agent': 'Holberton_School',
	    	    'Authorization': 'token ' + process.env.TOKEN
	    	}
	    }
	    req = https.request(user_options,function(stream){
		   combine(stream,action);
		});
	    req.end();
						      
	}

	var key_value = function(array,key,subkey){
	    var data = {};
	    var loc = {};
	    if(subkey){
		data = map.call(array[subkey],function(a) {
			var r = log(a,key);
			return r;
		    });
		return data;
	    } else {
		loc =  map.call(array,log);
		return loc;
	    }
	}
	    
	var parse = function(jsonString){
	    var array = {};
	    var array = JSON.parse(jsonString);
	    return array;
	}    

	var combine = function streamToString(stream, cb) {
	    const chunks = [];
	    var data;
	    stream.on('data', (chunk) => {
		    chunks.push(chunk);
		});
	    stream.on('end', () => {
		    cb(chunks.join(''));
		});
	}
	
	var action = function (jsonString) {
	    var array = parse(jsonString);
	    var result = {};
	    try { 
		array.items;
		var file = '/tmp/38';
		var result = key_value(array,'full_name','items');
	        process.env['RESULT'] = JSON.stringify(result);
		map.call(result,location);
	    } 
	    catch(err){
		var repo_array = JSON.parse(process.env.RESULT);
		process.env.REQUESTS = repo_array.length;
		var user = log(array,'login')['login'];
		var result = log(array,'location')['location'];
		var file = '/tmp/38';
		var push_obj = {};
		for(key in repo_array){
		    var key = key;
       		    var repo_user = repo_array[key]['full_name'];
		    if (repo_user.substr(0,user.length) == user){
			push_obj['full_name'] = repo_user;
			push_obj['location'] = result;
			final_obj.push(push_obj);
			process.env.COUNT++;
			waiting();
		       	return;
		    }
		}
	    }
	}
	combine(stream,action);
    }
    
var req = https.request(options, success);
req.end();

var waiting = function(){
    console.log(process.env.COUNT);
    if(process.env.REQUESTS == process.env.COUNT){
	var final_string = JSON.stringify(final_obj + '\n');
	fs.writeFile('/tmp/38',final_string);
	console.log("The file was saved!");
	clearInterval(print_interval);
    }
}