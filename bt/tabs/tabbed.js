if (window.parent && window.parent.synchTab)
	window.parent.synchTab(window.name);

function synchTab(frameName) {
  	var elList;
	var i;

  	// Exit if no frame name was given.

  	//if (frameName == null);
   		 //return;
	elList = document.getElementsByTagName("a");
	for(i = 0; i < elList.length; i++){
		if(elList[i].target == frameName){
			if(elList[i].href==window.frames[frameName].location.href){
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
