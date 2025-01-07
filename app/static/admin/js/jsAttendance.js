function getData() {
  // alert("1");
  const formData = new FormData();
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );
  formData.append("action", "getData");

  $.ajax({
    url: "/attendance_details/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {
      $("#tableData tr:gt(0)").remove();
      for (let i = 0; i < response.length; i++) {
        let j = i + 1;
        $("#tableData").append(
          "<tr><td>" +
            j +
            '</td><td style="display: none;">' +
            response[i].at_id +
            "</td><td>" +
            response[i].us_name +
            "</td><td>" +
            response[i].us_usn +
            "</td><td>" +
            response[i].cl_day_id +
            "</td><td>" +
            response[i].cl_time +
            "</td><td>" +
            response[i].cl_subject_id +
            "</td><td>YES</td></tr>"
        );
      }
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {},
  });
}

getData();
