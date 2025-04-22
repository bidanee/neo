function toggleMenu() {
  document.getElementById("sideMenu").classList.toggle("active");
}

function showPage(pageId) {
  document
    .querySelectorAll(".page")
    .forEach((p) => p.classList.remove("active"));
  document.getElementById(pageId).classList.add("active");
  toggleMenu(); // 메뉴 닫기
}

async function getExchangeRate() {
  try {
    const res = await fetch("http://192.168.1.15:8000/api/parties");
    const data = await res.json();
    console.log(res);
  } catch (error) {
    console.error(error);
  }
}

const countryNameToCode = {
  대한민국: "KR",
  미국: "US",
  일본: "JP",
  중국: "CN",
  영국: "GB",
  프랑스: "FR",
  독일: "DE",
  이탈리아: "IT",
  스페인: "ES",
  캐나다: "CA",
  호주: "AU",
};

document
  .getElementById("festivalsForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    const countryInput = document.getElementById("country").value.trim();
    let country = countryNameToCode[countryInput];

    if (!country) {
      alert("지원하지 않는 국가입니다. 예: 대한민국, 미국, 일본 등");
      return;
    }

    const start_date = document.getElementById("start_date").value;
    const end_date = document.getElementById("end_date").value;

    // Node 서버로 요청 (Node 서버가 FastAPI에 연결함)
    const res = await fetch(
      `/api/parties?country=${country}&start_date=${start_date}&end_date=${end_date}`
    );
    const data = await res.json();

    const container = document.getElementById("festivalsContainer");
    container.innerHTML = "";

    if (data.resultCode && data.festivals.length > 0) {
      data.festivals.forEach((festival) => {
        container.innerHTML += `
        <div>
          <h3>${festival.title}</h3>
          <p>${festival.description}</p>
          <p><strong>시작:</strong> ${festival.start} / <strong>종료:</strong> ${festival.end}</p>
          <hr>
        </div>
      `;
      });
    } else {
      container.innerHTML = `<p>조건에 맞는 축제가 없습니다.</p>`;
    }
  });

flatpickr("#start_date", {
  dateFormat: "Y-m-d",
  inline: true,
  locale: "ko",
});

flatpickr("#end_date", {
  dateFormat: "Y-m-d",
  inline: true,
  locale: "ko",
});

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("festivalsForm");
  const headline = document.querySelector(".slide-in-left.hol");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const festivals = [
      "🎉 삿포로 눈",
      "🎊 도쿄 여름 불꽃놀이",
      "🎭 교토 마츠리",
    ];

    // 축제 리스트를 <h1> 안에 추가
    headline.innerHTML += `
        <div>
          <h3>${festival.title}</h3>
          <p>${festival.description}</p>
          <p><strong>시작:</strong> ${festival.start} / <strong>종료:</strong> ${festival.end}</p>
          <hr>
        </div>
      `;
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const btnHoliday = document.getElementById("btnHoliday");
  const holidayTitle = document.getElementById("holidayTitle");

  btnHoliday.addEventListener("click", () => {
    // 숨기기 (애니메이션 효과 포함 가능)
    holidayTitle.style.display = "none";
  });
});
