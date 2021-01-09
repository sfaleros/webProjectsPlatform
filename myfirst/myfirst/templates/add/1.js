function isMobile() {
  return /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
}

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition;

class Recognizer {
  constructor() {
    this.recognition = new SpeechRecognition();
    this.recognition.lang = "en-GB";
    if (!isMobile()) {
      this.recognition.continuous = true;
      this.recognition.interimResults = true;
    }
    this.isRecognizing = false;
    this.transcript = "";
  }
  
  start(handler) {
    this.transcript = "";
    this.recognition.onresult = (event) => {
      this.onResult(event, handler);
    };
    this.recognition.start();
    this.isRecognizing = true;
    console.log("Started recognition");
  }
  
  stop() {
    this.recognition.abort();
    this.isRecognizing = false;
    console.log("Stopped recognition");
  }
  
  onResult(event, handler) {
    var interim_transcript = "";
    for (var i = event.resultIndex; i < event.results.length; ++i) {
      var result = event.results[i];
      if (result.isFinal) {
        this.transcript += result[0].transcript;
      } else {
        interim_transcript += result[0].transcript;
      }
    }
    console.log(interim_transcript);
    handler(interim_transcript);
  }
}

const btnRecognize = document.querySelector("#recognize");
const txtInterim = document.querySelector("#interim");
const txtMessage = document.querySelector("#message");
const recognizer = new Recognizer();

function showText(text) {
  txtInterim.value = text;
  txtMessage.value = recognizer.transcript;
}

function start() {
  txtInterim.value = "";
  txtMessage.value = "";
  recognizer.start(showText);
  btnRecognize.innerHTML = "Остановить запись";
}

function stop() {
  recognizer.stop();
  btnRecognize.innerHTML = "Начать запись";
}

btnRecognize.addEventListener("click", () => {
  if (!recognizer.isRecognizing) {
    start();
  } else {
    stop();
  }
});