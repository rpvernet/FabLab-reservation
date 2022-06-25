$("#id_type_reservation").change(function () {
    var url = $("#form").attr("data-durations-url");  // get the url of the `load_cities` view
    var type_reservation_Id = $(this).val();  // get the selected country ID from the HTML input

    $.ajax({                       // initialize an AJAX request
      url:'ajax/load-durations',                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      data: {
        'reservationID': type_reservation_Id       // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_cities` view function
        $("#id_duration").html(data);  // replace the contents of the city input with the data that came from the server
      }
    });

  });

