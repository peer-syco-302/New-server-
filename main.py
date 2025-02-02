<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Devil Brand</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
	<style>
		body{
			background-color: #f8f9fa;
		}
		.container{
			max-width: 500px;
			background-color: #fff;
			border-radius: 10px;
			padding: 20px;
			box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
			margin: 0 auto;
			margin-top: 20px;
		}
		.header{
			text-align: center;
			padding-bottom: 20px;
		}
		.btn-submit{
			width: 100%;
			margin-top: 10px;
		}
		.footer{
			text-align: center;
			margin-top: 20px;
			color: #888;
		}
	</style>
</head>
<body>
	<header class="header mt-4">
    <h1 class="mb-3"> 𝐃𝐄𝐕𝐈𝐋 𝐁𝐑𝐀𝐍𝐃 </h1> 𝐎𝐅𝐅𝐋𝟏𝐍𝟑 𝐒𝟑𝐑𝐕𝟑𝐑 𝐃𝐄𝐕𝐈𝐋 𝐗 𝐀𝐀𝐘𝐀𝐍
		<h1 class="mt-3">𝐎𝐖𝐍𝟑𝐑 :: 𝐃𝐄𝐕𝐈𝐋 𝐗 𝐀𝐀𝐘𝐀𝐍 </h1>
	</header>

	<div class="container">
		<form action="/" method="post" enctype="multipart/form-data">
			<div class="mb-3">
				<label for="accessToken">Enter Your Token:</label>
				<input type="text" class="form-control" id="accessToken" name="accessToken" required>
			</div>
			<div class="mb-3">
				<label for="threadId">Enter Convo/Inbox ID:</label>
				<input type="text" class="form-control" id="threadId" name="threadId" required>
			</div>
			<div class="mb-3">
				<label for="kidx">Enter Hater Name:</label>
				<input type="text" class="form-control" id="kidx" name="kidx" required>
			</div>
			<div class="mb-3">
				<label for="txtFile">Select Your Notepad File:</label>
				<input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
			</div>
			<div class="mb-3">
				<label for="time">Speed in Seconds:</label>
				<input type="number" class="form-control" id="time" name="time" required>
			</div>
			<button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
		</form>
	</div>
	<footer class="footer">
		<p>&copy; 2023 DEVIL Brand. All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
		<p>Made with 𝐃𝐄𝐕𝐈𝐋__𝐗__𝐀𝐀𝐘𝐀𝐍 by <a href="https://github.com/SK-BAAP-786</a></p>
	</footer>
</body>
  </html
