
  function alphaOnly(event) {
    let key = event.which ? event.which : event.keyCode;
    return (
      (key >= 65 && key <= 90) ||
      key == 8 ||
      (event.charCode >= 97 && event.charCode <= 122) ||
      event.charCode == 32
    );
  }
  
  $("#btn_add").click(function () {
    if ($("#txtName").val() == "") {
      alert("Please Enter Name");
      $("#txtName").focus();
      return false;
    }
  
    const formData = new FormData();
  
    formData.append("txtName", $("#txtName").val());
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
      url: "/days_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
        alert("Day added Successfully");
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
  
    if ($("#txtName1").val().trim().length < 1) {
      alert("Please Enter Name");
      $("#txtName11").focus();
      return false;
    }
  
    var formData = new FormData();
    formData.append("txtName1", $("#txtName1").val());
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
      url: "/days_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
        alert("Day Updated Succesfully");
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
  
      url: "/days_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function () {
        alert("Day deleted succesfully");
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
      url: "/days_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        $("#tableData tr:gt(0)").remove();
        for (var i = 0; i < response.length; i++) {
          var j = i + 1;
          $("#tableData").append(
            "<tr><td>" +
              j +
              '</td><td style="display: none;">' +
              response[i].day_id +
              "</td><td>" +
              response[i].day_name +
              "</td><td>" +
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
      var lclName = currentRow.find("td:eq(2)").text();
      // alert(lclName);
      $("#txtName1").val(lclName);
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
  