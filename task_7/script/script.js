function remoteCommand(cmd) {
  if (cmd === "docker run" || cmd === "docker exec") {
    // detached mode
    container_name = prompt("Name of the container: ");
    if (cmd === "docker run") {
      // AJAX call
      image = prompt("Enter the image name: ");
      console.log(cmd + " " + "-it " + image + " --name " + container_name);
    } else if (cmd === "docker rm -f") {
      console.log(cmd + " " + container_name);
    } else {
      command = prompt("Enter the command: ");
      console.log(cmd + " " + container_name + " " + command);
    }
  } else {
    // directly call the option
    console.log(cmd);
    commandCall(cmd);
  }
}

function typedCommand(event) {
  if (event.keyCode == 13) {
    var command = document.getElementById("textfield").value;
    console.log(command);
    commandCall(command);
    document.getElementById("textfield").value = "";
  }
}

function commandCall(cmd) {
  url = "http://192.168.0.105/cgi-bin/backend.py?cmd=";

  document.getElementById("text").innerHTML = "";
  var xhr = new XMLHttpRequest();
  // true is by default, calling it asynchronously
  xhr.open("GET", url + cmd, false);
  xhr.send();
  var output = xhr.responseText;
  console.log(output);
  document.getElementById("text").innerHTML = output;
}
