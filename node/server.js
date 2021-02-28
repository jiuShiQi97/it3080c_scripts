var fs = require("fs");
var http = require("http");
var os = require("os");
var ip = require("ip");



var server = http.createServer(function (req, res) {
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function (err, body) {
            res.writeHead(200, { "Cotnent-Type": "text/html" });
            res.end(body);
        });
    }

    else if (req.url.match("/sysinfo")) {
        myHostName = os.hostname();
        //turn the os.uptime to ISO method
        ServerUpTime = new Date(os.uptime() * 1000).toISOString().substr(11, 8);
        totalMem = os.totalmem()/1048576;
        freeMem = os.freemem()/1048576;
        cpus = os.cpus().length+1;
        html = `
        <!DOCTYPE html>

        <head>
            <title>sysinfo</title>
        </head>
        
        <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Up Time: ${ServerUpTime}</p>
            <p>Total Memory: ${totalMem} M</p>
            <p>Free Memory: ${freeMem} M</p>
            <p>Number of CPUs: ${cpus}</p>
        </body>
        
        </html>
        `
        res.writeHead( 200, { "Content-Type": "text/html" }); 
        res.end(html);
    }

    else {
        res.writeHead(404, { "Content-Type": "text/plain" });
        res.end(`404 File Not Found at ${req.url}`);
    }
});

server.listen(3000);
console.log("Server listening on port 3000");
