const divider = document.getElementById('divider');
const leftPanel = document.querySelector('.left-panel');
const rightPanel = document.querySelector('.right-panel');

let isDragging = false;

divider.addEventListener('mousedown', startDragging);
document.addEventListener('mousemove', drag);
document.addEventListener('mouseup', stopDragging);

function startDragging(e) {
  isDragging = true;
}

function drag(e) {
  if (!isDragging) return;

  const containerRect = divider.parentElement.getBoundingClientRect();
  const mouseX = e.clientX - containerRect.left;
  const containerWidth = containerRect.width;

  const leftPanelWidth = (mouseX / containerWidth) * 100;

  leftPanel.style.width = `${leftPanelWidth}%`;
}

function stopDragging() {
  isDragging = false;
  mouseX = 0;
  containerWidth = 0;
  leftPanelWidth = 0;
}
