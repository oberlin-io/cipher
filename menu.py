#!/usr/bin/python

html = '''Content-type: text/html

<html>
<head>
    <title>Cipher</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<meta name="viewport" content="width=device-width,initial-scale=1">
	<link rel="shortcut icon" href="http://oberl.info/images/ob.ico">
	<link href="https://fonts.googleapis.com/css?family=Do+Hyeon" rel="stylesheet">
    <style>
        body {
            max-width: 320px;
            margin: auto;
            font-family: 'Do Hyeon', sans-serif;
        }
        .button {
            width: 100%s;
            height: 40px;
            border-radius: 4px;
            background-color: black;
            color: white;
            vertical-align: middle;
            text-align: center;
            line-height: 40px;
        }
        a {
            text-decoration: none;
        }
        h1 {
            font-size: 50px;
            text-align: center;
        }
        img {
            width: 160px;
            margin-right: 80px;
            margin-left: 80px;
        }
    </style>
</head>
<body>
    <h1>Cipher</h1>
    <a href="enc.py"><div class="button">Encrypt</div></a><br>
    <a href="dec.py"><div class="button">Decrypt</div></a><br>
</body>
</html>
''' % "%"

print html
