document.getElementById('toggleBtn').addEventListener('click', function() {
    document.getElementById('navList').classList.toggle('open');
  });
  
window.addEventListener('load', function() {
    document.getElementById('navList').classList.add('open');
  });
function toggleNav() {
  var navList = document.getElementById("navList");
  navList.classList.toggle("open");
}
