// medicine module
(function(global) {
  var Medicine = function() {
    var medicine = {
      code: 0,
      name: ""
    };

    return {
      setCode: function(value) {
        medicine.code = value;
      },
      setName: function(value) {
        medicine.name = value;
      },
      setObject: function(object) {
        medicine = object;
      },
      getCode: function() {
        return medicine.code;
      },
      getName: function() {
        return medicine.name;
      },
      getObject: function() {
        return medicine;
      }
    };
  };

  global.Medicine = Medicine;
  global.medicines = [];
  global.$medicine;
}) (this);



$( document ).ready(function() {
  // get medicines
  $.ajax({
    type: 'GET',
    url: '/api/medicines/',
    contentType: 'application/json',
    processData: false
  })
  .done(function(data) {
    var mMedicines = data.results;
    for (var i = 0; i < mMedicines.length; i++) {
      var medicine = new Medicine();
      medicine.setObject(mMedicines[i]);

      medicines.push(medicine);
    }

    $medicine = createMedicineContainer(medicines);
    appendNewMedicament();
  });
});


$('#js-form').submit(function (evt) {
  evt.preventDefault();
  var btn = $('.js-submit');
  btn.button('loading');
  sendForm(function(isSendend) {
    btn.button('reset');
    if(isSendend){
      window.location = '/consultation/history/' + $('.js-dni').val() + '/';
    } else {
      alert('Ha ocurrido un error, revise el formulario por favor');
    }
  });
});

/*******************************************************************************************
*************************************    FUNCTIONS      ************************************
********************************************************************************************/

function createMedicineContainer(medicines) {
  var $medicine = $('.row-medicine').clone();
  $medicine.removeClass('clone');
  $medicine.show();

  var $select = $medicine.find('.js-select-medicine');
  
  // create an empty medicine
  var option = document.createElement("option");
  option.text = 'Sin medicamentos';
  $(option).appendTo($select);

  for (var i = 0; i < medicines.length; i++) {
    var option = document.createElement("option");
    option.text = medicines[i].getName();
    $(option).appendTo($select);
    $(option).attr('code', medicines[i].getCode());
  }

  return $medicine;
}

function appendNewMedicament() {
  var $mMedicine = $medicine.clone();
  $('.js-container-medicaments').append($mMedicine);
  
  $mMedicine.find('.js-add').on('click', function() {
    appendNewMedicament();
    $(this).hide();
    $mMedicine.find('.js-delete').show();
  });

  $mMedicine.find('.js-delete').on('click', function() {
    $(this).parents('.row').remove();
  });
}

function sendForm(callback) {
  var patient = $('.js-dni').val(),
      diagnosis = $('#diagnosis').val(),
      prescription = $('#prescription').val(),
      is_inpatient = $('#js-isInpatient').is(":checked");

  if(!diagnosis){
    callback(false);
    return;
  }

  $.ajax({
    url: '/api/consultations/',
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify({
      "patient": patient,
      "prescription": prescription,
      "diagnosis": diagnosis, 
      "is_inpatient": is_inpatient
    }),
    dataType: 'json',
    processData: false
  })
  .done(function(data) {
    sendMedicaments(data.id, callback);
  })
  .fail(function() {
    callback(false);
  });

}

function sendMedicaments(idConsult, callback) {
  var jsonArray = [];

  var $medicaments = $('.row-medicine:not(.clone)');
  for (var i = 0; i < $medicaments.length; i++) {
    
    var medicament = $($medicaments[i]).find('.js-select-medicine')[0],
        medicine = $(medicament.options[medicament.selectedIndex]).attr('code'),
        amount = $($medicaments[i]).find('.js-amount-medicine').val();

    if( medicine && amount){
      jsonArray.push({
        "medical_consultation": idConsult, 
        "medicine": medicine,
        "amount": amount
      });
    }
    
  }

  var total = jsonArray.length,
      conta = 0, 
      sendToApi = function(id) {
        $.ajax({
          url: '/api/medicines-per-consultation/',
          type: 'POST',
          contentType: 'application/json',
          data: JSON.stringify( jsonArray[id] ),
          dataType: 'json',
          processData: false

        })
        .done(function(data) {
          conta++;
          if (conta >= total) {
            callback(true);
          } else {
            sendToApi(conta);
          }
        })
        .fail(function() {
          callback(false);
        });
      };

  if(total > 0) {
    sendToApi(0);
  } else {
    callback(true);
  }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});