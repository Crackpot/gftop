<?php
    function amortizationTable($paymentNum,$periodicPayment,$balance,$monthlyInterest){
        $paymentInterest = round($balance * $monthlyInterest, 2);
        $paymentPrincipal = round($periodicPayment - $paymentInterest, 2);
        $newBlance = round($balance - $paymentPrincipal, 2);
        print "<tr>
            <td>$paymentNum</td>
            <td>\$".number_format($balance,2)."</td>
            <td>\$".number_format($periodicPayment,2)."</td>
            <td>\$".number_format($paymentInterest,2)."</td>
            <td>\$".number_format($paymentPrincipal,2)."</td>
            </tr>";
        # If balance not yet zero, recursively call amortizationTable()
        if ($newBlance > 0){
            $paymentNum ++;
            amortizationTable($paymentNum,$periodicPayment,$newBlance,$monthlyInterest);
        }else{
            exit;
        }
    }# end amortizationTable()
?>


<?php
    # Loan balance
    $balance = 200000.00;

    # Loan interest rate
    $interestRate = .0575;

    # Monthly interest rate
    $monthlyInterest = .0575/12;

    # Term length of the loan,in years.
    $termLength = 30;

    # Number of payment per year.
    $paymentPerYear = 12;

    # Payment interation
    $paymentNumber = 1;

    # Perform preliminary calculations
    $totalPayments = $termLength * $paymentPerYear;
    $intCalc = 1 + $interestRate / $paymentPerYear;
    $periodicPayment = $balance * pow($intCalc,$totalPayments) * ($intCalc - 1) / (pow($intCalc,$totalPayments) - 1);
    $periodicPayment = round($periodicPayment,2);

    # Create table
    echo "<table width='50%' aglin='center' border='1'>";
    print "<tr>
        <th>Payment Number</th><th>Balance</th><th>Payment</th><th>Interest</th><th>Principal</th>
        </tr>";
    #Call recursive function
    amortizationTable($paymentNumber,$periodicPayment,$balance,$monthlyInterest);
    #Close table
    echo "</table>";
?>


