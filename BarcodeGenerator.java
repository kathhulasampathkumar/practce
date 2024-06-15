
// import org.krysalis.barcode4j.impl.code128.Code128Bean;
// import org.krysalis.barcode4j.output.java2d.Java2DRenderer;
// import org.krysalis.barcode4j.tools.UnitConv;

// import java.awt.*;
// import java.awt.event.ActionEvent;
// import java.awt.event.ActionListener;
// import java.awt.print.*;

// public class BarcodeGenerator extends Frame implements ActionListener {
//     private TextField matCodeField, startSNField, endSNField;

//     public BarcodeGenerator() {
//         setTitle("Barcode Generator");
//         setSize(400, 200);

//         matCodeField = new TextField("Material Code");
//         startSNField = new TextField("Start Serial Number");
//         endSNField = new TextField("End Serial Number");

//         Button generateButton = new Button("Generate Barcode");
//         generateButton.addActionListener(this);

//         setLayout(new FlowLayout());
//         add(matCodeField);
//         add(startSNField);
//         add(endSNField);
//         add(generateButton);

//         addWindowListener(new java.awt.event.WindowAdapter() {
//             public void windowClosing(java.awt.event.WindowEvent windowEvent) {
//                 System.exit(0);
//             }
//         });
//     }

//     public void actionPerformed(ActionEvent e) {
//         if (e.getActionCommand().equals("Generate Barcode")) {
//             generateAndPrintBarcode();
//         }
//     }

//     private void generateAndPrintBarcode() {
//         String materialCode = matCodeField.getText();
//         int startSN = Integer.parseInt(startSNField.getText());
//         int endSN = Integer.parseInt(endSNField.getText());

//         for (int sn = startSN; sn <= endSN; sn++) {
//             String barcodeData = materialCode + "$" + sn;
//             generateBarcode(barcodeData);
//             printBarcode();
//         }
//     }

//     private void generateBarcode(String data) {
//         Code128Bean bean = new Code128Bean();
//         final int dpi = 150;
//         bean.setModuleWidth(UnitConv.in2mm(1.0f / dpi));
//         bean.doQuietZone(false);

//         try {
//             PrinterJob job = PrinterJob.getPrinterJob();
//             job.setPrintable(new Printable() {
//                 public int print(Graphics g, PageFormat pf, int pageIndex) {
//                     if (pageIndex > 0) {
//                         return NO_SUCH_PAGE;
//                     }

//                     Graphics2D g2d = (Graphics2D) g;
//                     g2d.translate(pf.getImageableX(), pf.getImageableY());

//                     Java2DRenderer renderer = new Java2DRenderer(g2d, 1, Color.BLACK, Color.WHITE);
//                     try {
//                         bean.generateBarcode(renderer, data);
//                     } catch (Exception e) {
//                         e.printStackTrace();
//                     }

//                     return PAGE_EXISTS;
//                 }
//             });

//             if (job.printDialog()) {
//                 job.print();
//             }
//         } catch (PrinterException e) {
//             e.printStackTrace();
//         }
//     }

//     public static void main(String[] args) {
//         BarcodeGenerator barcodeGenerator = new BarcodeGenerator();
//         barcodeGenerator.setVisible(true);
//     }
// }

