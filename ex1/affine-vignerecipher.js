function affineCipher() {
    let text = prompt("Enter the message to encrypt:");
    if (text === null || text === "") return;

    let a = 5;
    let b = 8;
    let a_inv = 21;

    let encrypted = "";
    let decrypted = "";
    let intermediate = "<b>Intermediate Encryption Steps:</b><br>";

    // Encryption
    for (let i = 0; i < text.length; i++) {
        let ch = text[i];
        if (ch >= 'A' && ch <= 'Z') {
            let x = ch.charCodeAt(0) - 65;
            let enc = (a * x + b) % 26;
            let res = String.fromCharCode(enc + 65);
            intermediate += `${ch} (val:${x}) -> (5*${x}+8)%26 = ${enc} (${res})<br>`;
            encrypted += res;
        }
        else if (ch >= 'a' && ch <= 'z') {
            let x = ch.charCodeAt(0) - 97;
            let enc = (a * x + b) % 26;
            let res = String.fromCharCode(enc + 97);
            intermediate += `${ch} (val:${x}) -> (5*${x}+8)%26 = ${enc} (${res})<br>`;
            encrypted += res;
        }
        else {
            encrypted += ch;
        }
    }

    // Decryption (Logic remains exactly yours)
    for (let i = 0; i < encrypted.length; i++) {
        let ch = encrypted[i];
        if (ch >= 'A' && ch <= 'Z') {
            let y = ch.charCodeAt(0) - 65;
            let dec = (a_inv * (y - b + 26)) % 26;
            decrypted += String.fromCharCode(dec + 65);
        }
        else if (ch >= 'a' && ch <= 'z') {
            let y = ch.charCodeAt(0) - 97;
            let dec = (a_inv * (y - b + 26)) % 26;
            decrypted += String.fromCharCode(dec + 97);
        }
        else {
            decrypted += ch;
        }
    }

    document.getElementById("result").innerHTML =
        "<b>Affine Cipher</b><br><br>" +
        intermediate + "<br>" +
        "Encrypted Text: " + encrypted + "<br>" +
        "Decrypted Text: " + decrypted;
}

// -------- VIGENERE CIPHER --------
function vigenereCipher() {
    let text = prompt("Enter the message:");
    let key = prompt("Enter the key:");
    if (text === null || key === null || text === "" || key === "") return;

    text = text.toUpperCase();
    key = key.toUpperCase();

    let encrypted = "";
    let decrypted = "";
    let keyMapping = ""; 
    let j = 0;

    // ENCRYPTION
    for (let i = 0; i < text.length; i++) {
        let ch = text[i];
        if (ch >= 'A' && ch <= 'Z') {
            let p = ch.charCodeAt(0) - 65;           
            let kChar = key[j % key.length];
            let k = kChar.charCodeAt(0) - 65; 

            keyMapping += kChar; 
            let c = (p + k) % 26;                    
            encrypted += String.fromCharCode(c + 65);
            j++;
        } else {
            encrypted += ch;
            keyMapping += " ";
        }
    }

    // DECRYPTION 
    j = 0;
    for (let i = 0; i < encrypted.length; i++) {
        let ch = encrypted[i];
        if (ch >= 'A' && ch <= 'Z') {
            let c = ch.charCodeAt(0) - 65;
            let k = key[j % key.length].charCodeAt(0) - 65;
            let p = (c - k + 26) % 26;
            decrypted += String.fromCharCode(p + 65);
            j++;
        } else {
            decrypted += ch;
        }
    }

    document.getElementById("result").innerHTML =
        "<b>Vigenere Cipher</b><br><br>" +
        "Intermediate Key Alignment:<br>" +
        "<pre>Text: " + text + "<br>Key:  " + keyMapping + "</pre><br>" +
        "Encrypted Text: " + encrypted + "<br>" +
        "Decrypted Text: " + decrypted;
}
