var app = require('http').createServer(handler)
var io = require('socket.io')(app);
var fs = require('fs');
var searchWords = [['bike', 'bicycle', 'bicicleta', 'bici', 'mountain', 'summer',
'vehicle', 'sport'],['book', 'literature', 'novel', 'harry', 'potter', 'luces',
'bohemia', 'george', 'orwell', '1984'],['cd', 'cds', 'music', 'disco', 'guitar',
'album', 'paco', 'metallica', 'duke']];

app.listen(3000);

function handler (req, res) {
    if (req.url == '/') {
        fs.readFile(__dirname + '/index.html',
        function (err, data) {
            if (err) {
                res.writeHead(500);
                return res.end('Error loading index.html');
            }

            var currentCookies = parseCookies(req);

            if (currentCookies['cart'] === undefined) {
                var d = new Date();
                d.setTime(d.getTime() + (1*24*60*60*1000));
                var expires = "expires="+ d.toUTCString();
                res.writeHead(200, {
                'Set-Cookie': 'cart=; ' + expires + '; path=/;'
                });
            } else {
                res.writeHead(200);
            }

            res.end(data);
        });

    } else if (req.url == '/buy') {
        if (req.method === 'POST') {
            let body = '';
            req.on('data', chunk => {
                body += chunk.toString(); // convert Buffer to string
            });
            req.on('end', () => {
                var name = body.split("&")[0].split("=")[1];
                res.end('Dear ' + name + ', your order has been received!');
            });
        }
    } else if (req.url.slice(0,7) == '/search') {
        var query = req.url.split('q=')[1];
        doSearch(query,res);

    } else if (req.url == '/autocomplete') {
        if (req.method == 'POST') {
            var body = '';
            req.on('data', function(chunk) {
                body += chunk.toString();
            });
            req.on('end', function() {
                var matchings = getWordsContaining(body);
                res.writeHead(200);
                res.end(matchings);
            });
        }

    } else {
        fs.readFile(__dirname + req.url,
            function (err, data) {
                if (err) {
                    res.writeHead(500);
                    return res.end('resource not found');
                }

                res.writeHead(200);
                res.end(data);
            });

    }
}

function parseCookies (request) {
    var list = {},
        rc = request.headers.cookie;

    rc && rc.split(';').forEach(function( cookie ) {
        var parts = cookie.split('=');
        list[parts.shift().trim()] = decodeURI(parts.join('='));
    });

    return list;
}

function doSearch(query,res) {
    var html = "/no-results.html"; // by default
    for (var i=0; i< searchWords.length; i++) {
        for (var j=0; j< searchWords[i].length; j++) {
            if (query == searchWords[i][j]) {
                switch(i) {
                    case 0:
                        html = "/bikes.html";
                        break;
                    case 1:
                        html = "/books.html";
                        break;
                    case 2:
                        html = "/cds.html";
                        break;
                    default:
                }
            }
        }
    }
    fs.readFile(__dirname + html,
    function (err, data) {
        if (err) {
            res.writeHead(500);
            return res.end('Error loading no-results.html');
        }

        res.writeHead(200);
        res.end(data);
    });
}

function getWordsContaining(text) {
    var related_names = "[";
    for (var i=0; i< searchWords.length; i++) {
        for (var j=0; j< searchWords[i].length; j++) {
            if (searchWords[i][j].includes(text)) {
                related_names += '"' + searchWords[i][j] + '",';
            }
        }
    }
    if (related_names.length >= 2) {
        related_names = related_names.slice(0, -1);
    }
    related_names += "]";
    return related_names;
}
