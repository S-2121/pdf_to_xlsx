import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15
import QtQuick.Layouts 2.15

import QtMultimedia 5.15


ApplicationWindow {
    id: window
    visible: true
    width: 600
    height: 500
    title: "성적표 처리 프로그램"
    
    Material.theme: Material.Dark
    Material.accent: Material.Orange
    // Material.foreground: Material.Grey
    // Material.primary: Material.Grey

    GridLayout {
        id: content_grid
        rows: 2
        columns: 1

        anchors.centerIn: parent
        
        columnSpacing: 20
        rowSpacing: 20
        Text {
            id: title_text
            text: qsTr("아래 버튼을 클릭하여 성적표 PDF 파일을 선택하세요.")
            color: Material.color(Material.Orange)
        }
        Button {
            id: select_file_button
            text: qsTr("파일 찾기")
            Material.foreground: Material.Orange
        }
    }

}