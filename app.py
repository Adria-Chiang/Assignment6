<!DOCTYPE html>
<head>
    <title>會員</title>
    <meta charset="utf-8"/>
    <style type="text/css">
        body{
            margin: 0px; 
        }
        .head{
            width: auto;height: 150px; background-color: #C39BD3;
            display: flex; align-items: center; justify-content: center; 
        }
        .content{
            text-align: center; margin-top: 30px; font-size: 25px;
        }

    </style>
</head>
<body>
    <div class="head">
        <h1>失敗頁面</h1>
    </div>
    <div class="content">
        {{message}}<br/>
        <a href="/">返回首頁</a>
    </div>
</body>
