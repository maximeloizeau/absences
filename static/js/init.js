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
});