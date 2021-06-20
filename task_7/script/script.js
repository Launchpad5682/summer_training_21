function remoteCommand(cmd) {
  if (cmd === "docker run" || cmd === "docker exec" || cmd === "docker rm -f") {
    // detached mode
    container_name = prompt("Name of the container: ");
    if (cmd === "docker run") {
      // AJAX call
      image = prompt("Enter the image name: ");
      cmd = cmd + " " + "-dt " + " --name " + container_name + " " + image;
      console.log(cmd);
      commandCall(cmd);
    } else if (cmd === "docker rm -f") {
      cmd = cmd + " " + container_name;
      console.log(cmd);
      commandCall(cmd);
    } else {
      command = prompt("Enter the command: ");
      cmd = cmd + " " + container_name + " " + command;
      console.log(cmd);
      commandCall(cmd);
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
