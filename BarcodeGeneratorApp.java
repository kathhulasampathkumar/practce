// import java.awt.*;
// import java.awt.event.ActionEvent;
// import java.awt.event.ActionListener;
// import java.lang.foreign.GroupLayout;

// public class BarcodeGeneratorApp {
//     private Frame frame;
//     private TextField matCodeField;
//     private TextField startSlNoField;
//     private TextField endSlNoField;

//     public static void main(String[] args) {
//         EventQueue.invokeLater(() -> {
//             try {
//                 BarcodeGeneratorApp window = new BarcodeGeneratorApp();
//                 window.frame.setVisible(true);
//             } catch (Exception e) {
//                 e.printStackTrace();
//             }
//         });
//     }

//     public BarcodeGeneratorApp() {
//         initialize();
//     }

//     private void initialize() {
//         frame = new Frame();
//         frame.setBounds(100, 100, 450, 300);
//         frame.setTitle("Barcode Generator");

//         matCodeField = new TextField();
//         startSlNoField = new TextField();
//         endSlNoField = new TextField();

//         Label matCodeLabel = new Label("Material Code:");
//         Label startSlNoLabel = new Label("Start Sl. No:");
//         Label endSlNoLabel = new Label("End Sl. No:");

//         Button generateBarcodeButton = new Button("Generate Barcode");
//         generateBarcodeButton.addActionListener(new ActionListener() {
//             @Override
//             public void actionPerformed(ActionEvent e) {
//                 String matCode = matCodeField.getText();
//                 String startSlNo = startSlNoField.getText();
//                 String endSlNo = endSlNoField.getText();

//                 // Add logic for barcode generation and printing here

//                 // For now, let's print the values
//                 System.out.println("Material Code: " + matCode);
//                 System.out.println("Start Sl. No: " + startSlNo);
//                 System.out.println("End Sl. No: " + endSlNo);
//             }
//         });

//         Panel panel = new Panel();
//         GroupLayout layout = new GroupLayout(panel);
//         panel.setLayout(layout);

//         layout.setAutoCreateGaps(true);
//         layout.setAutoCreateContainerGaps(true);

//         GroupLayout.SequentialGroup hGroup = layout.createSequentialGroup();
//         hGroup.addGroup(layout.createParallelGroup()
//                 .addComponent(matCodeLabel)
//                 .addComponent(startSlNoLabel)
//                 .addComponent(endSlNoLabel)
//                 .addComponent(generateBarcodeButton));

//         hGroup.addGroup(layout.createParallelGroup()
//                 .addComponent(matCodeField)
//                 .addComponent(startSlNoField)
//                 .addComponent(endSlNoField));

//         layout.setHorizontalGroup(hGroup);

//         GroupLayout.SequentialGroup vGroup = layout.createSequentialGroup();
//         vGroup.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
//                 .addComponent(matCodeLabel)
//                 .addComponent(matCodeField));
//         vGroup.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
//                 .addComponent(startSlNoLabel)
//                 .addComponent(startSlNoField));
//         vGroup.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
//                 .addComponent(endSlNoLabel)
//                 .addComponent(endSlNoField));
//         vGroup.addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
//                 .addComponent(generateBarcodeButton));

//         layout.setVerticalGroup(vGroup);

//         frame.add(panel);

//         frame.addWindowListener(new java.awt.event.WindowAdapter() {
//             public void windowClosing(java.awt.event.WindowEvent windowEvent) {
//                 System.exit(0);
//             }
//         });
//     }
// }
