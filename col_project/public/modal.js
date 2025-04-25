// 요소 선택
const modal = document.getElementById("my-modal");
const openBtn = document.getElementById("open-modal");
const closeBtn = document.querySelector(".close");

// 열기
openBtn.onclick = function () {
  modal.style.display = "block";
};

// 닫기 (X 버튼)
closeBtn.onclick = function () {
  modal.style.display = "none";
};

// 바깥 클릭 시 닫기
window.onclick = function (event) {
  if (event.target === modal) {
    modal.style.display = "none";
  }
};
