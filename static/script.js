document.addEventListener("DOMContentLoaded", () => {
    const filter = document.getElementById("severityFilter");
    const bugs = document.querySelectorAll(".bug-item");
  
    filter?.addEventListener("change", () => {
      const selected = filter.value;
      bugs.forEach(bug => {
        if (!selected || bug.dataset.severity === selected) {
          bug.style.display = "";
        } else {
          bug.style.display = "none";
        }
      });
    });
  });  
