const express = require("express");
const fileUpload = require("express"); 
const pdfParse = require("pdf-parse");

const app = express();

app.use("/", express.static("templates"));
app.use(fileUpload());

app.post("/extract-text", (req, res) => {
    if (req.files && !req.files.pdfFile) {
        req.status(400);
        res.end();
    }

    pdfParse(req.files.pdfFile).then(result => {
        res.send(result.text)
    })
});

app.listen(3000);


