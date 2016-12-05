function init() {
	$("#prelude").show();
	if (navigator.appVersion.indexOf("Android") > -1 && navigator.appVersion.indexOf("Chrome") > -1) {
		$("#email").on("focus", function() {
			$("#prelude").hide();
		});
		$("#password").on("focus", function() {
			$("#prelude").hide();
		});
		$("#confirm").on("focus", function() {
			$("#prelude").hide();
		});
	}
}
