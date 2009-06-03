if (window.parent && window.parent.synchTab)
	window.parent.synchTab(window.name);

function synchTab(frameName) {
	//alert("insynchTab");
	//alert(frameName);
  	var elList;
	var i;

  	// Exit if no frame name was given.

  	//if (frameName == null);
   		 //return;
	//alert("did Not return");
	elList = document.getElementsByTagName("a");
	for(i = 0; i < elList.length; i++){
		//alert('hi');
		//alert(elList[i].target);
		if(elList[i].target == frameName){
			//alert("target == frameName");
			//alert(elList[i].target);
			//alert(frameName);
			//alert(elList[i].href);
			//alert(window.frames[frameName].location);
			if(elList[i].href==window.frames[frameName].location.href){
				//alert("href something");
				elList[i].className += " activeTab";
				elList[i].blur();
			}
			else
				removeName(elList[i], "activeTab");
		}
	}
}

function removeName(el, name) {
	var i, curList, newList;

	newList = new Array();
	curList = el.className.split(" ");
	for (i = 0; i < curList.length; i++)
		if (curList[i] != name)
			newList.push(curList[i]);
	el.className = newList.join(" ");
}
