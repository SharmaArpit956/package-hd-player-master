
http = require("socket.http")
ltn12 = require("ltn12")

res, code = http.request{
    url = 'https://api-v2.voicemonkey.io/announcement?token=66893dd2d71897629dfed1300a4ff16d_024f29e75cf0a203694b92a88263e304&device=alexa-tts&text= Hello node',
    method = "GET",
    source = ltn12.source.string('key=value'),
}

if code == 200 then
    print(res)
else
    print("HTTP request failed")
end
