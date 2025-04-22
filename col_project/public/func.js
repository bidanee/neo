// document
//   .getElementById("exchange-form")
//   .addEventListener("submit", function (e) {
//     e.preventDefault(); // 폼 기본 동작 방지

//     const country = document.getElementById("exchange-country").value;

//     // 현재 환율 요청
//     fetch(`/rcurrent_exchange_rate?country=${encodeURIComponent(country)}`)
//       .then((res) => res.json())
//       .then((data) => {
//         const resultDiv = document.getElementById("result-exchange");

//         if (data.error) {
//           resultDiv.innerHTML = `<p style="color:red;">❌ ${data.error}</p>`;
//           return;
//         }

//         const date = data["날짜"];
//         const formattedDate = `${date.slice(0, 4)}년 ${date.slice(
//           4,
//           6
//         )}월 ${date.slice(6)}일`;

//         resultDiv.innerHTML = `
//           <p><strong>${formattedDate}</strong> 기준 ${country}의 환율은 <strong>${data["환율"]} ${data["통화코드"]}</strong>입니다.</p>
//           <p>📊 아래는 최근 1년간 환율 변동 차트입니다!</p>
//         `;
//       })
//       .catch((error) => {
//         console.error("오류 발생:", error);
//         document.getElementById("result-exchange").innerHTML =
//           "<p style='color:red;'>❌ 오류가 발생했습니다.</p>";
//       });

//     // 차트 이미지 요청
//     document.getElementById(
//       "exchange-chart"
//     ).src = `/rexchange_rate?country=${encodeURIComponent(country)}`;
//   });

document
  .getElementById("exchange-form")
  .addEventListener("submit", function (e) {
    e.preventDefault(); // 폼 기본 동작 방지

    const country = document.getElementById("exchange-country").value;

    // 현재 환율 요청
    fetch(`/exchange_rate?country=${encodeURIComponent(country)}`)
      .then((res) => res.json())
      .then((data) => {
        const resultDiv = document.getElementById("result-exchange");

        if (data.error) {
          resultDiv.innerHTML = `<p style="color:red;">❌ ${data.error}</p>`;
          return;
        }

        const chartData = data;
        const ctx = document.getElementById("exchange-chart").getContext("2d");
        const chart = new Chart(ctx, {
          type: "line",
          data: chartData,
          options: {},
        });

        resultDiv.innerHTML = `
          <p>📊 아래는 최근 1년간 환율 변동 차트입니다!</p>
        `;
      })
      .catch((error) => {
        console.error("오류 발생:", error);
        document.getElementById("result-exchange").innerHTML =
          "<p style='color:red;'>❌ 오류가 발생했습니다.</p>";
      });
  });
