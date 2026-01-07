import javax.swing.*;
import javax.swing.border.TitledBorder;
import javax.swing.text.DefaultCaret;
import java.awt.*;
import java.awt.event.*;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class BrowserSimulatorDSA {

    // GUI Components
    private JFrame frame;
    private JTextField urlField;
    private JButton visitBtn, openBtn, backBtn, forwardBtn, homeBtn, reportBtn, currentBtn;
    private JTextArea backArea, forwardArea, countsArea, currentArea;
    private JLabel visitsLabel, backOpsLabel, forwardOpsLabel;

    // DSA Structures
    private String currentURL = "https://google.com";
    private Stack<String> backStack = new Stack<>();
    private Stack<String> forwardStack = new Stack<>();
    private Map<String, Integer> visitCounts = new HashMap<>();
    private int totalVisits = 1, backOps = 0, forwardOps = 0;

    public BrowserSimulatorDSA() {
        visitCounts.put(currentURL, 1);
        setupGUI();
        updateDisplay();
    }

    private void setupGUI() {
        frame = new JFrame("DSA Lab: Browser History Simulator");
        frame.setSize(1200, 800);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        // Top Panel - Title
        JLabel title = new JLabel("📚 DSA Lab: Browser History Simulator", SwingConstants.CENTER);
        title.setFont(new Font("Arial", Font.BOLD, 22));
        title.setOpaque(true);
        title.setBackground(new Color(0, 0, 128));
        title.setForeground(Color.WHITE);
        title.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        frame.add(title, BorderLayout.NORTH);

        // Stats Panel
        JPanel statsPanel = new JPanel(new FlowLayout(FlowLayout.LEFT, 20, 5));
        visitsLabel = new JLabel("Total Visits: 1");
        backOpsLabel = new JLabel("Back: 0");
        forwardOpsLabel = new JLabel("Forward: 0");
        visitsLabel.setFont(new Font("Arial", Font.BOLD, 16));
        backOpsLabel.setFont(new Font("Arial", Font.BOLD, 16));
        forwardOpsLabel.setFont(new Font("Arial", Font.BOLD, 16));
        statsPanel.add(visitsLabel);
        statsPanel.add(backOpsLabel);
        statsPanel.add(forwardOpsLabel);
        frame.add(statsPanel, BorderLayout.SOUTH);

        // Center Panel - Main Grid 2x2
        JPanel mainPanel = new JPanel(new GridLayout(2, 2, 10, 10));
        mainPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        // Current Page
        currentArea = new JTextArea();
        currentArea.setEditable(false);
        currentArea.setFont(new Font("Arial", Font.BOLD, 16));
        currentArea.setLineWrap(true);
        currentArea.setWrapStyleWord(true);
        JScrollPane currentScroll = new JScrollPane(currentArea);
        TitledBorder currentBorder = BorderFactory.createTitledBorder("📱 Current Page");
        currentBorder.setTitleFont(new Font("Arial", Font.BOLD, 16));
        currentScroll.setBorder(currentBorder);
        mainPanel.add(currentScroll);

        // Visit Counts
        countsArea = new JTextArea();
        countsArea.setEditable(false);
        countsArea.setFont(new Font("Courier New", Font.PLAIN, 14));
        JScrollPane countsScroll = new JScrollPane(countsArea);
        TitledBorder countsBorder = BorderFactory.createTitledBorder("🔢 Visit Counts");
        countsBorder.setTitleFont(new Font("Arial", Font.BOLD, 16));
        countsScroll.setBorder(countsBorder);
        mainPanel.add(countsScroll);

        // Back Stack
        backArea = new JTextArea();
        backArea.setEditable(false);
        backArea.setFont(new Font("Courier New", Font.PLAIN, 14));
        JScrollPane backScroll = new JScrollPane(backArea);
        TitledBorder backBorder = BorderFactory.createTitledBorder("⬅️ Back Stack");
        backBorder.setTitleFont(new Font("Arial", Font.BOLD, 16));
        backScroll.setBorder(backBorder);
        mainPanel.add(backScroll);

        // Forward Stack
        forwardArea = new JTextArea();
        forwardArea.setEditable(false);
        forwardArea.setFont(new Font("Courier New", Font.PLAIN, 14));
        JScrollPane forwardScroll = new JScrollPane(forwardArea);
        TitledBorder forwardBorder = BorderFactory.createTitledBorder("➡️ Forward Stack");
        forwardBorder.setTitleFont(new Font("Arial", Font.BOLD, 16));
        forwardScroll.setBorder(forwardBorder);
        mainPanel.add(forwardScroll);

        frame.add(mainPanel, BorderLayout.CENTER);

        // Top Controls
        JPanel controlPanel = new JPanel();
        controlPanel.setLayout(new FlowLayout(FlowLayout.LEFT, 10, 10));
        urlField = new JTextField("youtube.com", 30);
        visitBtn = new JButton("Visit");
        openBtn = new JButton("Open");
        backBtn = new JButton("⬅️ Back");
        forwardBtn = new JButton("➡️ Forward");
        homeBtn = new JButton("🏠 Home");
        reportBtn = new JButton("📊 Report");
        currentBtn = new JButton("🔗 Current");

        controlPanel.add(new JLabel("URL:"));
        controlPanel.add(urlField);
        controlPanel.add(visitBtn);
        controlPanel.add(openBtn);
        controlPanel.add(backBtn);
        controlPanel.add(currentBtn);
        controlPanel.add(forwardBtn);
        controlPanel.add(homeBtn);
        controlPanel.add(reportBtn);

        frame.add(controlPanel, BorderLayout.NORTH);

        // Button Actions
        visitBtn.addActionListener(e -> visitURL());
        openBtn.addActionListener(e -> openInBrowser());
        backBtn.addActionListener(e -> goBack());
        forwardBtn.addActionListener(e -> goForward());
        homeBtn.addActionListener(e -> goHome());
        reportBtn.addActionListener(e -> saveReport());
        currentBtn.addActionListener(e -> openCurrent());

        frame.setVisible(true);
    }

    private void visitURL() {
        String url = urlField.getText().trim();
        if (url.isEmpty()) {
            JOptionPane.showMessageDialog(frame, "Enter a URL!");
            return;
        }
        if (!url.startsWith("http://") && !url.startsWith("https://")) {
            url = "https://" + url;
        }
        backStack.push(currentURL);
        currentURL = url;
        visitCounts.put(url, visitCounts.getOrDefault(url, 0) + 1);
        totalVisits++;
        visitsLabel.setText("Total Visits: " + totalVisits);
        urlField.setText("");
        forwardStack.clear(); // Visiting new page clears forward stack
        updateDisplay();
    }

    private void openInBrowser() {
        try {
            visitURL();
            Desktop.getDesktop().browse(new java.net.URI(currentURL));
        } catch (Exception e) {
            JOptionPane.showMessageDialog(frame, "Cannot open URL: " + e.getMessage());
        }
    }

    private void goBack() {
        if (!backStack.isEmpty()) {
            forwardStack.push(currentURL);
            currentURL = backStack.pop();
            backOps++;
            backOpsLabel.setText("Back: " + backOps);
            updateDisplay();
        } else {
            JOptionPane.showMessageDialog(frame, "No previous pages!");
        }
    }

    private void goForward() {
        if (!forwardStack.isEmpty()) {
            backStack.push(currentURL);
            currentURL = forwardStack.pop();
            forwardOps++;
            forwardOpsLabel.setText("Forward: " + forwardOps);
            updateDisplay();
        } else {
            JOptionPane.showMessageDialog(frame, "No forward pages!");
        }
    }

    private void goHome() {
        backStack.clear();
        forwardStack.clear();
        currentURL = "https://google.com";
        visitCounts.clear();
        visitCounts.put(currentURL, 1);
        totalVisits = 1;
        backOps = 0;
        forwardOps = 0;
        visitsLabel.setText("Total Visits: 1");
        backOpsLabel.setText("Back: 0");
        forwardOpsLabel.setText("Forward: 0");
        urlField.setText("");
        updateDisplay();
    }

    private void openCurrent() {
        try {
            Desktop.getDesktop().browse(new java.net.URI(currentURL));
        } catch (Exception e) {
            JOptionPane.showMessageDialog(frame, "Cannot open URL: " + e.getMessage());
        }
    }

    private void saveReport() {
        try {
            StringBuilder html = new StringBuilder();
            html.append("<html><head><title>DSA Lab Report</title></head><body>");
            html.append("<h1>Browser History Report</h1>");
            html.append("<h2>Current Page</h2>");
            html.append("<p>").append(currentURL).append("</p>");
            html.append("<h2>Visit Counts</h2><ol>");
            visitCounts.entrySet().stream()
                    .sorted((a, b) -> b.getValue() - a.getValue())
                    .limit(15)
                    .forEach(entry -> html.append("<li>").append(entry.getKey())
                            .append(" → ").append(entry.getValue()).append("</li>"));
            html.append("</ol>");
            html.append("<h2>Back Stack</h2><p>").append(backStack).append("</p>");
            html.append("<h2>Forward Stack</h2><p>").append(forwardStack).append("</p>");
            html.append("<h2>Statistics</h2>");
            html.append("<p>Total Visits: ").append(totalVisits).append("</p>");
            html.append("<p>Back Operations: ").append(backOps).append("</p>");
            html.append("<p>Forward Operations: ").append(forwardOps).append("</p>");
            html.append("</body></html>");

            FileWriter writer = new FileWriter("DSA_Report.html");
            writer.write(html.toString());
            writer.close();
            Desktop.getDesktop().browse(new java.io.File("DSA_Report.html").toURI());
            JOptionPane.showMessageDialog(frame, "✅ Report Created Successfully!");
        } catch (IOException e) {
            JOptionPane.showMessageDialog(frame, "❌ Error: " + e.getMessage());
        }
    }

    private void updateDisplay() {
        // Current
        currentArea.setText("📱 " + currentURL + " (" + visitCounts.get(currentURL) + " visits)");

        // Counts
        countsArea.setText("");
        visitCounts.entrySet().stream()
                .sorted((a, b) -> b.getValue() - a.getValue())
                .limit(12)
                .forEach(entry -> countsArea.append(entry.getKey() + " → " + entry.getValue() + "\n"));

        // Back Stack
        backArea.setText("");
        if (backStack.isEmpty()) backArea.setText("🚫 EMPTY");
        else {
            int i = 1;
            for (int j = backStack.size() - 1; j >= 0; j--) {
                backArea.append(i++ + ". " + backStack.get(j) + "\n");
            }
        }

        // Forward Stack
        forwardArea.setText("");
        if (forwardStack.isEmpty()) forwardArea.setText("🚫 NO FORWARD PAGES");
        else {
            int i = 1;
            for (String s : forwardStack) forwardArea.append(i++ + ". " + s + "\n");
        }

        backBtn.setEnabled(!backStack.isEmpty());
        forwardBtn.setEnabled(!forwardStack.isEmpty());
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(BrowserSimulatorDSA::new);
    }
}