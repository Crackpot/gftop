class BuzzwordsReport extends Report {

    void runReport() {
        super.runReport(); //调用父类的方法
        buzzwordCompliance();
        printReport();
    }

    void buzzwordCompliance() {
        System.out.println("buzzwordCompliance");
    }

    public static void main(String[] args) {
        BuzzwordsReport BuzzwordsReportInstance = new BuzzwordsReport();
        BuzzwordsReportInstance.runReport();
    }
}
