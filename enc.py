#!/usr/bin/python

import cgi


top = '''Content-type: text/html

<html>
    <title>Cipher</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
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
        input {
            width: 100%s;
	}
	td {
	    width: 160px;
	}
    </style>
<head>
</head>
<body>
    <h1>Cipher</h1>
    <p><a href="menu.py">&lt; back</a></p>
''' % ("%", "%")

form = cgi.FieldStorage()

form_html = '''    <form action='enc.py' method='get'>
		<table>
			<tr>
				<td><label for='raw_str'>Input</label></td>
				<td><input type='text' name='raw_str' id='raw_str'></td>
			</tr>
			<tr>
				<td><label for='key'>Key phrase</label></td>
				<td><input type='text' name='key' id='key'></td>
			</tr>
		<tr>
		<td colspan="2">
		 </td>
		</tr>
		<td colspan="2">
		<input type='submit' name='ok' class='button' value='ENCRYPT'></td>
		</tr>
		<td colspan="2">
		 </td>
		</tr>
'''


print top
print form_html

txt = form['raw_str'].value
key = form['key'].value

ascii = {   " ":"0100000",
            "!":"0100001",
            "\"":"0100010",
            "#":"0100011",
            "$":"0100100",
            "%":"0100101",
            "&":"0100110",
            "'":"0100111",
            "(":"0101000",
            ")":"0101001",
            "*":"0101010",
            "+":"0101011",
            ",":"0101100",
            "-":"0101101",
            ".":"0101110",
            "/":"0101111",
            "0":"0110000",
            "1":"0110001",
            "2":"0110010",
            "3":"0110011",
            "4":"0110100",
            "5":"0110101",
            "6":"0110110",
            "7":"0110111",
            "8":"0111000",
            "9":"0111001",
            ":":"0111010",
            ";":"0111011",
            "<":"0111100",
            "=":"0111101",
            ">":"0111110",
            "?":"0111111",
            "@":"1000000",
            "A":"1000001",
            "B":"1000010",
            "C":"1000011",
            "D":"1000100",
            "E":"1000101",
            "F":"1000110",
            "G":"1000111",
            "H":"1001000",
            "I":"1001001",
            "J":"1001010",
            "K":"1001011",
            "L":"1001100",
            "M":"1001101",
            "N":"1001110",
            "O":"1001111",
            "P":"1010000",
            "Q":"1010001",
            "R":"1010010",
            "S":"1010011",
            "T":"1010100",
            "U":"1010101",
            "V":"1010110",
            "W":"1010111",
            "X":"1011000",
            "Y":"1011001",
            "Z":"1011010",
            "[":"1011011",
            "\\":"1011100",
            "]":"1011101",
            "^":"1011110",
            "_":"1011111",
            "`":"1100000",
            "a":"1100001",
            "b":"1100010",
            "c":"1100011",
            "d":"1100100",
            "e":"1100101",
            "f":"1100110",
            "g":"1100111",
            "h":"1101000",
            "i":"1101001",
            "j":"1101010",
            "k":"1101011",
            "l":"1101100",
            "m":"1101101",
            "n":"1101110",
            "o":"1101111",
            "p":"1110000",
            "q":"1110001",
            "r":"1110010",
            "s":"1110011",
            "t":"1110100",
            "u":"1110101",
            "v":"1110110",
            "w":"1110111",
            "x":"1111000",
            "y":"1111001",
            "z":"1111010",
            "{":"1111011",
            "|":"1111100",
            "}":"1111101",
            "~":"1111110",
}



bi_text = ""

for c in txt:
    bi_text += ascii.get(c,c)



if len(txt) > len(key):

    bi_key = ""
    for c in key:
        bi_key += ascii.get(c,c)

    mod = len(bi_text) % len(bi_key)

    short = len(bi_text) - mod

    mult = short / len(bi_key)

    bi_key = bi_key * mult
    bi_key += bi_key[:mod]

else:
    key = key[:len(txt)]
    bi_key = ""
    for c in key:
        bi_key += ascii.get(c,c)




bi_enc = ""
for i in range(len(bi_text)):
    xor = (int(bi_text[i]) and not int(bi_key[i])) or (not int(bi_text[i]) and int(bi_key[i]))
    if xor == True:
        bi_enc += "1"
    else:
        bi_enc += "0"




print '''<tr><td colspan="2">Encrypted</td></tr>
<tr><td colspan="2"><input type='text' value="%s"></td></tr>
</form>
''' % bi_enc
