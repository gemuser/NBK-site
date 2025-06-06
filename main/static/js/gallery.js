let slideIndex = 0;
showSlides();

function showSlides() {
  let slides = document.getElementsByClassName("slide");
  for (let i = 0; i < slides.length; i++) slides[i].style.display = "none";
  slideIndex++;
  if (slideIndex > slides.length) slideIndex = 1;
  if (slides.length > 0) slides[slideIndex - 1].style.display = "block";
  setTimeout(showSlides, 3000); // Change every 3s
}

function plusSlides(n) {
  slideIndex += n - 1;
  showSlides();
}
