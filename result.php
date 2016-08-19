<!doctype html>
<?php
// 调用Python模块执行爬虫功能和写入数据库功能
$keywords = iconv("UTF-8","GBK",$_POST["keywords"]);
exec('python ./novelbase.py '.$keywords);
?>
<html class="no-js" lang="en">
<head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" /> 
	<title>猎书搜索报告</title>
	<link rel="stylesheet" href="css/normalize.css">
	<link rel="stylesheet" href="css/grid.css">
	<link rel="stylesheet" href="css/flexslider.css">
	<link rel="stylesheet" href="css/style.css">
	<script>document.cookie='resolution='+Math.max(screen.width,screen.height)+'; path=/';</script>
	<script src="js/libs/modernizr.custom.min.js"></script>
</head>
<body id="home">
<div id="features" class="container"></div>
	<section id="content" role="main" class="container">
		<div class="two-columns">
			<div class="striped-heading span12">
				<h1>猎书搜索报告</h1>
				<div class="decoration"></div>
			</div>

            <?php
            header("Content-Type: text/html;charset=utf-8");
            $con = mysql_connect("localhost","root","");
            mysql_query("set character set 'utf8'");//读库 
            mysql_query("set names 'utf8'");//写库 
            mysql_select_db("test", $con);
            $sql = str_replace("keywords", $_POST["keywords"], "SELECT * FROM book WHERE KEYWORDS = 'keywords' ORDER BY I asc");
            $result = mysql_query($sql);
            $row = mysql_fetch_array($result);
            while($row = mysql_fetch_array($result))
            {
                echo "<div class=\"span6\">";
                echo "<div class=\"media\">";
                echo str_replace("#", $row['URL'], "<a href = \"#\" class=\"object\" data-hover=\"icon-play\" target = \"_blank\">");
                echo str_replace("#", $row['IMG'], "<img src=\"#\" style=\"width:96px;height:120px;\"></a>");
                echo "<div class=\"caption\">";
                echo str_replace("#", $row['URL'], "<a href = \"#\" class=\"object\" data-hover=\"icon-play\" target = \"_blank\">");
                echo str_replace("#", $row['TITLE'], "<h3>#</h3></a>");
                echo "<div class=\"hr_small\"></div>";
                echo "<p>".$row['AUTHOR']."</p>";
				echo "<p>状态：".$row['STATUS']."</p>";
                echo "<p>".$row['CONTENT']."</p>";
                echo "</div>";
                echo "</div>";
                echo "</div>";
            }
            ?>
		</div>
        
	</section>

<script>window.jQuery || document.write('<script src="js/libs/jquery-1.7.1.min.js"><\/script>')</script>
<script src="js/plugins.js"></script>
<script src="js/script.js"></script>
</body>
</html>
