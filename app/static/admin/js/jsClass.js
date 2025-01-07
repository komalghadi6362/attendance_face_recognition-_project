
  
  $("#btn_add").click(function () {
    if ($("#txtTime").val() == "") {
      alert("Please Enter Name");
      $("#txtTime").focus();
      return false;
    }

    if ($("#selDays").val() == "") {
      alert("Please Enter Class Day");
      $("#selDays").focus();
      return false;
    }

    if ($("#selFaculty").val() == "") {
      alert("Please Enter Class Faculty");
      $("#selFaculty").focus();
      return false;
    }

    if ($("#selSubject").val() == "") {
      alert("Please Enter Class Subject");
      $("#selSubject").focus();
      return false;
    }
  
    
  
    const formData = new FormData();
  
    formData.append("txtTime", $("#txtTime").val());
    formData.append("selDays", $("#selDays").val());
    formData.append("selFaculty", $("#selFaculty").val());
    formData.append("selSubject", $("#selSubject").val());
    formData.append(
      "csrfmiddlewaretoken",
      $("input[name=csrfmiddlewaretoken]").val()
    );
    formData.append("action", "add");
  
    // console.log(typeof(formData));
  
    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_add").attr("disabled", true);
      },
      url: "/class_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
        alert("Class Timing Added Successfully");
        location.reload();
        $("#add_modal").modal("hide");
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {
        $(".btn .spinner-border").hide();
        $("#btn_add").attr("disabled", false);
      },
    });
  });
  
  $(document).on("click", "#btn_update", function () {
    // alert("hi");
  
    if ($("#txtTime1").val().trim().length < 1) {
      alert("Please Enter Class Timing");
      $("#txtTime1").focus();
      return false;
    }

    if ($("#selDays1").val().trim().length < 1) {
      alert("Please Enter Class Day");
      $("#selDays1").focus();
      return false;
    }

    if ($("#selFaculty1").val().trim().length < 1) {
      alert("Please Enter Class Faculty");
      $("#selFaculty1").focus();
      return false;
    }

    if ($("#selSubject1").val().trim().length < 1) {
      alert("Please Enter Class Subject");
      $("#selSubject1").focus();
      return false;
    }
  
  
    var formData = new FormData();
    formData.append("txtTime1", $("#txtTime1").val());
    formData.append("selDays1", $("#selDays1").val());
    formData.append("selFaculty1", $("#selFaculty1").val());
    formData.append("selSubject1", $("#selSubject1").val());
    formData.append("id", $("#edit_id").val());
    formData.append(
      "csrfmiddlewaretoken",
      $("input[name=csrfmiddlewaretoken]").val()
    );
    formData.append("action", "update");
  
    // var table = $("#dataTables-example").DataTable();
  
    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_update").attr("disabled", true);
      },
      url: "/class_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
        alert("Class Details Updated Succesfully");
        location.reload();
        table.ajax.reload();
        $("#edit_modal").modal("hide");
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {
        $(".btn .spinner-border").hide();
        $("#btn_update").attr("disabled", false);
      },
    });
  });
  
  //Delete work step
  $(document).on("click", "#btn_delete", function () {
    var formData = new FormData();
    formData.append("id", $("#delete_id").val());
    formData.append(
      "csrfmiddlewaretoken",
      $("input[name=csrfmiddlewaretoken]").val()
    );
    formData.append("action", "delete");
  
    // var table = $("#dataTables-example").DataTable();
  
    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
      },
  
      url: "/class_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function () {
        alert("Class Details deleted succesfully");
        location.reload();
        table.ajax.reload();
        $("#delete_modal").modal("hide");
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {
        $(".btn .spinner-border").hide();
        // Reset Form
        //$("#view_field_form")[0].reset();
        $(".close").click();
      },
    });
  });
  
  function getData() {
    // alert("1");
    var formData = new FormData();
    formData.append(
      "csrfmiddlewaretoken",
      $("input[name=csrfmiddlewaretoken]").val()
    );
    formData.append("action", "getData");
  
    $.ajax({
      url: "/class_details/",
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
              response[i].cl_id +
              "</td><td>" +
              response[i].cl_time +
              "</td><td>" +
              response[i].cl_day_id +
              "</td><td>" +
              response[i].cl_faculty_id +
              "</td><td>" +
              response[i].cl_subject_id +
              '</td><td><div class="d-flex" style="justify-content: space-evenly;"><a href="javascript:void(0);" id="edit_row" title="View/Edit" data-toggle="modal" data-target="#edit_modal" class="text-primary" onClick="getRowsUpdate();"> <i class="fa fa-edit"></i></a><a href="javascript:void(0);" title="Delete" data-bs-toggle="modal" data-bs-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();"> <i class="far fa-trash-alt"></i></a></div></td></tr>'
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
  
  function getRowsUpdate() {
    $("#tableData tr").click(function () {
      var currentRow = $(this).closest("tr");
      var lclID = currentRow.find("td:eq(1)").text();
      var lclTime= currentRow.find("td:eq(2)").text();
      var lclDayId= currentRow.find("td:eq(3)").text();
      var lclFacultyId = currentRow.find("td:eq(4)").text();
      var lclSubjectId = currentRow.find("td:eq(5)").text();
      // alert(lclName);
      $("#txtTime1").val(lclTime);
      $("#selDays1").val(lclDayId);
      $("#selFaculty1").val(lclFacultyId);
      $("#selSubject1").val(lclSubjectId);
      $("#edit_id").val(lclID);
  
      $("#edit_modal").modal("show");
    });
  }
  
  function getRowsDelete() {
    $("#tableData tr").click(function () {
      var currentRow = $(this).closest("tr");
      var lclID = currentRow.find("td:eq(1)").text();
      // alert(lclID);
      $("#delete_id").val(lclID);
    });
  }
  





  function getDaysData() {
    // alert("1");
    var formData = new FormData();
    formData.append(
      "csrfmiddlewaretoken",
      $("input[name=csrfmiddlewaretoken]").val()
    );
    formData.append("action", "getData");
  
    $.ajax({
      url: "/days_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        for (let i = 0; i < response.length; i++) {
          let j = i + 1;
          $("#selDays").append("<option value='"+response[i].day_name+"'>"+response[i].day_name+"</option>");
          $("#selDays1").append("<option value='"+response[i].day_name+"'>"+response[i].day_name+"</option>");
        }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {},
    });
  }
  
  getDaysData();






  function getFacultyData() {
    // alert("1");
    var formData = new FormData();
    formData.append(
      "csrfmiddlewaretoken",
      $("input[name=csrfmiddlewaretoken]").val()
    );
    formData.append("action", "getData");
  
    $.ajax({
      url: "/faculty_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        
        for (var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#selFaculty").append("<option value='"+response[i].fc_name+"'>"+response[i].fc_name+"</option>");
          $("#selFaculty1").append("<option value='"+response[i].fc_name+"'>"+response[i].fc_name+"</option>");
        }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {},
    });
  }
  
  getFacultyData();







  function getSubjectData() {
    // alert("1");
    var formData = new FormData();
    formData.append(
      "csrfmiddlewaretoken",
      $("input[name=csrfmiddlewaretoken]").val()
    );
    formData.append("action", "getData");
  
    $.ajax({
      url: "/subject_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        for (var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#selSubject").append("<option value='"+response[i].su_name+"'>"+response[i].su_name+"</option>");
          $("#selSubject1").append("<option value='"+response[i].su_name+"'>"+response[i].su_name+"</option>");
        }
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {},
    });
  }
  
  getSubjectData();