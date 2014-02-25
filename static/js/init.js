$(document).ready(function() {

	$("#id_role").change(function() {
		var val = $(this).val();
		if(val == 1) {
			$("#id_annee").parent().show();
			$("#id_dpt").parent().hide();
			$("#id_respo_annee").parent().hide();
		}
		else if(val == 4) {
			$("#id_annee").parent().hide();
			$("#id_dpt").parent().hide();
			$("#id_respo_annee").parent().show();
		}
		else if(val == 5) {
			$("#id_annee").parent().hide();
			$("#id_dpt").parent().show();
			$("#id_respo_annee").parent().hide();
		}
		else {
			$("#id_annee").parent().hide();
			$("#id_dpt").parent().hide();
			$("#id_respo_annee").parent().hide();
		}
	});
	$("#id_role").change();

	$("input[name='date']").datetimepicker();

	$(".multiple-control").chosen();
	$("ul.chosen-choices").addClass("form-control");

	$("div#etudiant_select select").change(function() {
		$.get("/api/absences/list/" + $(this).val(), function(data) {
			var select = $("div#absences_etudiant select");
			select.empty();
			console.log(data);
			for(var i = 0; i < data.length; i++) {
				select.append('<option value="' + data[i].id + '">' + data[i].matiere + ' ' + data[i].date + '</option>');
			}

			$(".multiple-control").trigger('chosen:updated');
		});
	});
	$("div#etudiant_select select").change();
});