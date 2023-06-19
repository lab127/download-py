/**
 * buat new blank spreadsheet
 * klik extension -> app script
 * buat file script baru, dan beri nama baru
 * kopi paste kode `listFolderContents`
 * ganti `foldername` dengan folder yang diinginkan
 * save project
 * run project -> review permission
 * hasil file spreadsheet berada di root folder google drive dengan nama `ListOfFiles_{foldername}`
 * 
 */

function listFolderContents() {
    var foldername = 'public'; // ganti public jadi nama folder yang diinginkan
    var ListOfFiles = 'ListOfFiles_' + foldername;

    var folders = DriveApp.getFoldersByName(foldername)
    var folder = folders.next();
    var contents = folder.getFiles();

    var ss = SpreadsheetApp.create(ListOfFiles); // buat spreadsheet result
    var sheet = ss.getActiveSheet();
    sheet.appendRow( ['name', 'link', 'id', 'sizeInMB'] ); // row header

    var var_file;
    var var_name;
    var var_link;
    var var_size;

    while(contents.hasNext()) {
        var_file = contents.next();
        var_name = var_file.getName();
        var_link = var_file.getUrl();
        var_id = var_file.getId();
        var_size=var_file.getSize()/1024.0/1024.0;
        sheet.appendRow( [var_name, var_link, var_id, var_size] ); // append header 
    }
};
