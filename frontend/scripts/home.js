//Why was this file created???
//Why did I do this???
//I don't know...
//
//Is there some use for this... hmmm...
// Smoothly fade in the main container
window.addEventListener("DOMContentLoaded", () => {
    const container = document.querySelector(".container");
    if (container) {
      container.style.opacity = 0;
      container.style.transition = "opacity 1s ease-in";
      setTimeout(() => (container.style.opacity = 1), 100);
    }
    
    updateClock();
    setInterval(updateClock, 1000);
  });
  
  // Live clock
  function updateClock() {
    const clock = document.getElementById("clock");
    if (clock) {
      clock.textContent = new Date().toLocaleTimeString();
    }
  }
  
  // Fun quote generator
  const quotes = [
    "Keep pushing forward 🚀",
    "Bug today, boss tomorrow.",
    "Code. Sleep. Debug. Repeat.",
    "The terminal is your best friend.",
    "Commit like nobody's watching."
  ];
  
  document.addEventListener("click", () => {
    const q = document.getElementById("quote");
    if (q) {
      q.textContent = quotes[Math.floor(Math.random() * quotes.length)];
    }
  });
  
  // Theme toggle
  document.getElementById("themeToggle")?.addEventListener("click", () => {
    document.body.classList.toggle("dark");
  });
  