let chartInstance = null;

document
  .getElementById("exchange-form")
  .addEventListener("submit", function (e) {
    e.preventDefault();

    const originLeft = document.querySelector(".left-origin");
    originLeft.classList.add("noshow");

    const country = document.getElementById("country-exchange").value;

    // 현재 환율 정보 불러오기
    fetch(`/rcurrent_exchange_rate?country=${country}`)
      .then((res) => res.json())
      .then((data) => {
        const resultDiv = document.getElementById("result-exchange");

        if (data.error) {
          resultDiv.innerHTML = `<p style="color:red;">❌ ${data.error}</p>`;
          return;
        }

        const current_rate = parseFloat(data["환율"]); // ✅ 현재 환율 저장
        const currency_code = data["통화코드"];
        const date = data["날짜"];
        const formattedDate = `${date.slice(0, 4)}. ${date.slice(
          4,
          6
        )}. ${date.slice(6)}일`;

        resultDiv.innerHTML = `
          <div>
            <h2 style="font-weight: 800;">${formattedDate} </h2>
          </div>
          <p> ${country}의 환율은 <strong>${current_rate} ${currency_code}</strong>입니다.</p>
          <p>📊 최근 환율 정보!!!</p>
        `;

        // ✅ 과거 환율 데이터와 차트 생성
        return fetch(`/rexchange_rate?country=${country}`)
          .then((res) => res.json())
          .then((data) => {
            if (data.error) {
              alert(data.error);
              return;
            }

            const labels = data.labels.map(
              (d) =>
                `${d.slice(0, 4)}.${d.slice(4, 6).padStart(2, "0")}.${d
                  .slice(6)
                  .padStart(2, "0")}`
            );

            const datasets = data.datasets;

            // ✅ 현재 환율 기준선 추가
            datasets.push({
              label: "현재 환율",
              data: new Array(labels.length).fill(current_rate),
              borderColor: "#36a2eb",
              borderWidth: 2,
              borderDash: [5, 5],
              pointRadius: 0,
            });

            const ctx = document
              .getElementById("exchange-chart")
              .getContext("2d");

            if (chartInstance) {
              chartInstance.destroy();
            }

            chartInstance = new Chart(ctx, {
              type: "line",
              data: {
                labels: labels,
                datasets: datasets,
              },
              options: {
                responsive: true,
                scales: {
                  y: {
                    beginAtZero: false,
                  },
                },
                plugins: {
                  backgroundColorPlugin: true,
                },
              },
              plugins: [
                {
                  id: "backgroundColorPlugin",
                  beforeDraw: function (chart) {
                    const ctx = chart.ctx;
                    ctx.save();
                    ctx.fillStyle = "#f0f8ff"; // 배경색 설정
                    ctx.fillRect(0, 0, chart.width, chart.height);
                    ctx.restore();
                  },
                },
              ],
            });
          });
      })
      .catch((error) => {
        console.error("오류 발생:", error);
        document.getElementById("result-exchange").innerHTML =
          "<p style='color:red;'>❌ 오류가 발생했습니다.</p>";
      });
  });
