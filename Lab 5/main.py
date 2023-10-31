import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from mathmy import Math

class MathApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Math Functions App")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Function documentation and example will appear here.")
        layout.addWidget(self.label)

        button_styles = (
            "border-radius: 16px;"
            "background-color: #18A999;"
            "padding: 8px;"
            "font-size: 14px;"
            "font-weight: 700;"
            "color: #FFFFFF;"
        )

        functions = {
            "Normal Distribution": Math.normal_distribution,
            "Sigmoid Function": Math.sigmoid,
            "Logistic Regression Weight Update": Math.logistic_regression_weight_update,
            "Mean Squared Error": Math.mean_squared_error,
            "Cross-Entropy Loss": Math.cross_entropy_loss,
        }

        for function_name, function in functions.items():
            button = QPushButton(function_name)
            button.setStyleSheet(button_styles)
            button.clicked.connect(lambda _, func=function: self.show_docstring_and_example(func))
            layout.addWidget(button)

        self.setLayout(layout)

    def show_docstring_and_example(self, function):
        docstring = function.__doc__
        example = "Example:\n" + docstring.split("Example:")[1] if "Example:" in docstring else ""
        self.label.setText(docstring + "\n" + example)

def main():
    app = QApplication(sys.argv)
    window = MathApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
