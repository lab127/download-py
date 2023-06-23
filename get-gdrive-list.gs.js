/**
 * buat new blank spreadsheet, kemudian beri nama
 * klik extension -> app script
 * buat file script baru, dan beri nama baru
 * kopi paste kode `daftarFile`
 * ganti `id-folder` dengan folder id yang diinginkan
 * save project
 * run project -> review permission
 * hasil file spreadsheet setelah eksekusi selesai
*/

function daftarFile() {
	// gunakan aktif sheet
	var sh = SpreadsheetApp.getActiveSheet();
	// id folder bisa dilihat di url
	var folder = DriveApp.getFolderById('id-folder');
	var list = [];
	// nama kolom
	list.push(['Name','ID','Size']);
	var files = folder.getFiles();
	// loop files
	while (files.hasNext()){
	file = files.next();
		var row = []
		row.push(file.getName(),file.getId(),file.getSize())
		list.push(row);
	}
	sh.getRange(1,1,list.length,list[0].length).setValues(list);
}
