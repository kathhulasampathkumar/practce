
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimpleCalculator extends Frame implements ActionListener {

    private TextField textField;
    private String operator;
    private double num1, num2, result;

    public SimpleCalculator() {
        setTitle("Simple Calculator");
        setSize(400, 500);
        setLayout(new BorderLayout());

        textField = new TextField();
        add(textField, BorderLayout.NORTH);

        Panel buttonPanel = new Panel();
        buttonPanel.setLayout(new GridLayout(4, 4));

        String[] buttonLabels = {
                "7", "8", "9", "/",
                "4", "5", "6", "*",
                "1", "2", "3", "-",
                "0", ".", "=", "+"
        };

        for (String label : buttonLabels) {
            Button button = new Button(label);
            button.addActionListener(this);
            buttonPanel.add(button);
        }

        add(buttonPanel, BorderLayout.CENTER);

        // setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main(String[] args) {
        new SimpleCalculator();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();

        if (Character.isDigit(command.charAt(0)) || command.equals(".")) {
            textField.setText(textField.getText() + command);
        } else if (command.equals("C")) {
            textField.setText("");
            num1 = num2 = result = 0;
            operator = null;
        } else if (command.equals("=")) {
            num2 = Double.parseDouble(textField.getText());
            calculate();
            textField.setText(String.valueOf(result));
            num1 = result;
            operator = null;
        } else {
            if (operator != null) {
                num2 = Double.parseDouble(textField.getText());
                calculate();
                num1 = result;
            } else {
                num1 = Double.parseDouble(textField.getText());
            }
            operator = command;
            textField.setText("");
        }
    }

    private void calculate() {
        switch (operator) {
            case "+":
                result = num1 + num2;
                break;
            case "-":
                result = num1 - num2;
                break;
            case "*":
                result = num1 * num2;
                break;
            case "/":
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    textField.setText("Error");
                    num1 = num2 = result = 0;
                    operator = null;
                    return;
                }
                break;
        }
    }
}

