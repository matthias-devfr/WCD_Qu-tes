const audio = document.querySelector('audio');

audio.load();

document.addEventListener('click', e => {
  audio.currentTime = 0;
  audio.play();
})