function validateEmail(paramEmailID) {
  let filter = /^[0-9a-z.]+\@[a-z0-9]+\.[a-zA-z0-9]{2,4}$/;

  if (filter.test(paramEmailID)) {
    return true;
  } else {
    return false;
  }
}
function alphaOnly(event) {
  let key = event.which ? event.which : event.keyCode;
  return (
    (key >= 65 && key <= 90) ||
    key == 8 ||
    (event.charCode >= 97 && event.charCode <= 122) ||
    event.charCode == 32
  );
}
function isNumberKey(evt) {
  let charCode = evt.which ? evt.which : event.keyCode;
  if (charCode > 31 && (charCode < 48 || charCode > 57)) {
    return false;
  }
  return true;
}

$("#btn_add").click(function () {
  if ($("#txtUsn").val() == "") {
    alert("Please Enter Usn");
    $("#txtUsn").focus();
    return false;
  }

  if ($("#txtName").val() == "") {
    alert("Please Enter Name");
    $("#txtName").focus();
    return false;
  }

  if ($("#txtEmail").val() == "") {
    alert("Please Enter Email");
    $("#txtEmail").focus();
    return false;
  }

  if ($("#txtMobileNo").val() == "") {
    alert("Please Enter your Mobile number");
    $("#txtMobileNo").focus();
    return false;
  }

  if ($("#txtAddress").val() == "") {
    alert("Please Enter Address");
    $("#txtAddress").focus();
    return false;
  }

  if ($("#txtParentEmail").val() == "") {
    alert("Please Enter Parent Email");
    $("#txtParentEmail").focus();
    return false;
  }

  const formData = new FormData();

  formData.append("txtUsn", $("#txtUsn").val());
  formData.append("txtName", $("#txtName").val());
  formData.append("txtEmail", $("#txtEmail").val());
  formData.append("txtMobileNo", $("#txtMobileNo").val());
  formData.append("txtAddress", $("#txtAddress").val());
  formData.append("txtParentEmail", $("#txtParentEmail").val());
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
    url: "/student_details/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (res) {
      if (res == "10") {
        alert("Student already present");
      } else {
        alert("Student Added Successfully");
        location.reload();
        $("#add_modal").modal("hide");
      }
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

  if ($("#txtUsn1").val().trim().length < 1) {
    alert("Please Enter Usn");
    $("#txtUsn1").focus();
    return false;
  }

  if ($("#txtName1").val().trim().length < 1) {
    alert("Please Enter Name");
    $("#txtName1").focus();
    return false;
  }

  if ($("#txtEmail1").val().trim().length < 1) {
    alert("Please Enter Email");
    $("#txtEmail1").focus();
    return false;
  }

  if ($("#txtMobileNo1").val().trim().length < 10) {
    alert("Please Enter Correct Mobile Number");
    $("#txtMobileNo1").focus();
    return false;
  }

  if ($("#txtAddress1").val().trim().length < 1) {
    alert("Please Enter Address");
    $("#txtAddress1").focus();
    return false;
  }

  if ($("#txtParentEmail1").val().trim().length < 1) {
    alert("Please Enter Email");
    $("#txtParentEmail1").focus();
    return false;
  }

  var formData = new FormData();
  formData.append("txtUsn1", $("#txtUsn1").val());
  formData.append("txtName1", $("#txtName1").val());
  formData.append("txtMobileNo1", $("#txtMobileNo1").val());
  formData.append("txtEmail1", $("#txtEmail1").val());
  formData.append("txtAddress1", $("#txtAddress1").val());
  formData.append("txtParentEmail1", $("#txtParentEmail1").val());
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
    url: "/student_details/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (result) {
      alert("Student Details Updated Succesfully");
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
  let formData = new FormData();
  formData.append("id", $("#delete_id").val());
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );
  formData.append("action", "delete");

  $.ajax({
    beforeSend: function () {
      $(".btn .spinner-border").show();
    },

    url: "/student_details/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function () {
      alert("Student Details deleted succesfully");
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
    url: "/student_details/",
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
            response[i].us_id +
            "</td><td>" +
            response[i].us_usn +
            "</td><td>" +
            response[i].us_name +
            "</td><td>" +
            response[i].us_email +
            "</td><td>" +
            response[i].us_mobile +
            "</td><td>" +
            response[i].us_address +
            "</td><td>" +
            response[i].us_parent_email +
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
    let currentRow = $(this).closest("tr");
    let lclID = currentRow.find("td:eq(1)").text();
    let lclUsn = currentRow.find("td:eq(2)").text();
    let lclName = currentRow.find("td:eq(3)").text();
    let lclMobile = currentRow.find("td:eq(5)").text();
    let lclEmail = currentRow.find("td:eq(4)").text();
    let lclAddress = currentRow.find("td:eq(6)").text();
    let lclParentEmail = currentRow.find("td:eq(7)").text();
    // alert(lclName);
    $("#txtUsn1").val(lclUsn);
    $("#txtName1").val(lclName);
    $("#txtMobileNo1").val(lclMobile);
    $("#txtEmail1").val(lclEmail);
    $("#txtAddress1").val(lclAddress);
    $("#txtParentEmail1").val(lclParentEmail);
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

function trainModel() {
  const formData = new FormData();
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );

  $.ajax({
    beforeSend: function () {
      $("#btnTrainModel").html("Model Training...");
    },

    url: "/train_model/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function () {
      alert("Model Trained successfully");
      location.reload();
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {
      $("#btnTrainModel").html("Model Training Completed...");
    },
  });
}
