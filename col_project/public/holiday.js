function showPage(pageId) {
  document
    .querySelectorAll(".page")
    .forEach((p) => p.classList.remove("active"));
  document.getElementById(pageId).classList.add("active");
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
  const headline = document.getElementById(".resultBox");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    // 축제 리스트를 <h1> 안에 추가
    headline.innerHTML += `
    <div>
      <h3>${festival.title}</h3>
      <p>${festival.description}</p>
      <p><strong>시작:</strong> ${festival.start} / <strong>종료:</strong> ${festival.end}</p>
    </div>
  `;
  });
});

const btnHoliday = document.getElementById("btnHoliday");
const holidayTitle = document.getElementById("holidayTitle");
const countryInput = document.getElementById("country");

btnHoliday.addEventListener("click", () => {
  let country = document.getElementById("country").value.trim();

  if (country) {
    holidayTitle.innerHTML = `<div><span style="color: #16cba7; background-color: white; border-radius: 5px">"${country}"</span> 축제에 관한 내용 보여줄게!</div>`;
  } else {
    holidayTitle.innerHTML = `어느 나라 축제를 찾고 있니? 나라 이름을 입력해줘!`;
  }

  e.preventDefault();

  country = countryInput.value.trim();
  if (country) {
    // 텍스트 바꾸기
    holidayTitle.innerHTML = `"${country}" 축제에 관한 내용 보여줄게!`;

    // 정렬 상태 해제 (중앙 정렬 삭제용 클래스 추가/제거)
    document.querySelector(".left-panel.holiday").classList.remove("centered");
  }
});

btnHoliday.addEventListener("click", (s) => {
  const country = countryInput.value.trim();

  if (country) {
    // 초기 중앙 화면 숨기기
    holidayInitial.classList.add("hidden");

    // 결과용 제목 보이기 + 내용 변경
    holidayTitle.innserHTML = `<div><span style="color: #16cba7; background-color: white; border-radius: 5px">"${country}"</span> 축제에 관한 내용 보여줄게!</div>`;
    holidayTitle.classList.remove("hidden");
    holidayIcon.classList.remove("hidden");
  }
});

const ctx = document.getElementById("chartCanvas").getContext("2d");
const apiKey = "YjZA4Mwc2DPMFUfMkZvJcaGfjsTUdWcO"; // 여기에 본인의 Ticketmaster API 키 입력

const countryToCode = {
  일본: "JP",
  미국: "US",
  베트남: "VN",
};

const labels = [
  "2022-01",
  "2022-02",
  "2022-03",
  "2022-04",
  "2022-05",
  "2022-06",
  "2022-07",
  "2022-08",
  "2022-09",
  "2022-10",
  "2022-11",
  "2022-12",
  "2023-01",
  "2023-02",
  "2023-03",
  "2023-04",
  "2023-05",
  "2023-06",
  "2023-07",
  "2023-08",
  "2023-09",
  "2023-10",
  "2023-11",
  "2023-12",
  "2024-01",
  "2024-02",
  "2024-03",
  "2024-04",
  "2024-05",
  "2024-06",
  "2024-07",
];

const travelerData = {
  일본: Array(31)
    .fill()
    .map((_, i) => 100000 + i * 1000),
  미국: Array(31)
    .fill()
    .map((_, i) => 500000 + i * 2000),
  베트남: Array(31)
    .fill()
    .map((_, i) => 300000 + i * 1500),
};

const chartConfig = {
  type: "bar",
  data: {
    labels: labels,
    datasets: [],
  },
  options: {
    responsive: true,
    scales: {
      y: {
        type: "linear",
        position: "left",
        title: { display: true, text: "출국자 수" },
      },
      y1: {
        type: "linear",
        position: "right",
        title: { display: true, text: "축제 개수" },
        grid: { drawOnChartArea: false },
        ticks: { stepSize: 1 },
      },
    },
    plugins: {
      annotation: { annotations: {} },
      legend: { display: true },
    },
  },
};

const chart = new Chart(ctx, chartConfig);

async function fetchFestivals(countryCode) {
  const today = new Date().toISOString().split("T")[0];
  const url = `https://app.ticketmaster.com/discovery/v2/events.json?egmentName=Music,Sports,Arts&startDateTime=2022-01-01T00:00:00Z&endDateTime=2024-12-07T23:59:59Z&size=200&page=0&apikey=YjZA4Mwc2DPMFUfMkZvJcaGfjsTUdWcO`;

  try {
    const res = await fetch(url);
    const data = await res.json();
    return data._embedded?.events || [];
  } catch (err) {
    console.error("API Error:", err);
    return [];
  }
}

function extractFestivalMonths(events) {
  const counts = {};
  for (let i = 0; i < labels.length; i++) {
    counts[labels[i]] = 0;
  }

  events.forEach((e) => {
    const dt = new Date(e.dates?.start?.dateTime);
    const ym = `${dt.getFullYear()}-${String(dt.getMonth() + 1).padStart(
      2,
      "0"
    )}`;
    if (counts[ym] !== undefined) {
      counts[ym]++;
    }
  });

  return labels.map((month) => counts[month] || 0);
}

function createAnnotations(monthsWithFestivals) {
  return Object.fromEntries(
    monthsWithFestivals
      .map((count, i) => {
        if (count > 0) {
          return [
            `line${i}`,
            {
              type: "line",
              xMin: i,
              xMax: i,
              borderColor: "red",
              borderDash: [5, 5],
              borderWidth: 2,
              label: {
                content: "축제",
                enabled: true,
                position: "start",
                color: "red",
                backgroundColor: "white",
              },
            },
          ];
        }
      })
      .filter(Boolean)
  );
}

async function updateChart(country) {
  const travelers = travelerData[country];
  const countryCode = countryToCode[country];

  const events = await fetchFestivals(countryCode);
  const festCounts = extractFestivalMonths(events);
  const annotations = createAnnotations(festCounts);

  chart.data.datasets = [
    {
      label: `${country} 출국자 수`,
      data: travelers,
      type: "line",
      borderColor: "rgba(54, 162, 235, 1)",
      backgroundColor: "rgba(54, 162, 235, 0.2)",
      yAxisID: "y",
      tension: 0.4,
    },
    {
      label: "축제 개수",
      data: festCounts,
      backgroundColor: "rgba(255, 99, 132, 0.5)",
      yAxisID: "y1",
    },
  ];

  chart.options.plugins.annotation.annotations = annotations;
  chart.update();
}

document.getElementById("country").addEventListener("change", (e) => {
  updateChart(e.target.value);
});

// 초기 로드
updateChart("미국");
