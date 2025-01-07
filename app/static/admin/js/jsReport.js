function getData() {
  if ($("#selMonth").val() == "") {
    alert("Please Select Month");
    $("#selMonth").focus();
    return false;
  }

  if ($("#selYear").val() == "") {
    alert("Please Select Year");
    $("#selYear").focus();
    return false;
  }
  const formData = new FormData();
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );
  formData.append("selMonth", $("#selMonth").val());
  formData.append("selYear", $("#selYear").val());
  formData.append("action", "getData");

  $.ajax({
    url: "/report_details/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {
      $("#tableData tr:gt(0)").remove();
      for (let i = 0; i < response.length; i++) {
        let j = i + 1;
        if (response.length) {
          reportData = response;
          let xValues = reportData.map((item) => item.us_name);
          let yValues = reportData.map((item) => item.total_attendance);
          let barColors = ["yello", "green", "blue", "orange", "brown"]; // You can customize this based on your preference

          // Creating the chart
          new Chart("myChart", {
            type: "bar",
            data: {
              labels: xValues,
              datasets: [
                {
                  backgroundColor: barColors.slice(0, xValues.length),
                  data: yValues,
                },
              ],
            },
            options: {
              scales: {
                yAxes: [
                  {
                    ticks: {
                      beginAtZero: true, // Start the Y-axis at 0
                      suggestedMin: 0, // Ensure the minimum value is 0
                    },
                  },
                ],
              },
              legend: { display: false },
              title: {
                display: true,
                text: "Attendance Report",
              },
            },
          });
        } else {
          $("#tableData").append("<tr><td>No Records Found...</td></tr>");
        }
      }
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {},
  });
}

// let xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
// let yValues = [55, 49, 44, 24, 15];
// let barColors = ["red", "green", "blue", "orange", "brown"];

// new Chart("myChart", {
//   type: "bar",
//   data: {
//     labels: xValues,
//     datasets: [
//       {
//         backgroundColor: barColors,
//         data: yValues,
//       },
//     ],
//   },
//   options: {
//     legend: { display: false },
//     title: {
//       display: true,
//       text: "World Wine Production 2018",
//     },
//   },
// });
