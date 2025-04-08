document.addEventListener("DOMContentLoaded", function () {
    const canvas = document.getElementById('progressChart');
    const passed = parseInt(canvas.dataset.passed);
    const failed = parseInt(canvas.dataset.failed);

    new Chart(canvas.getContext('2d'), {
        type: 'pie',
        data: {
            labels: ['Passed', 'Failed'],
            datasets: [{
                data: [passed, failed],
                backgroundColor: ['rgba(40, 167, 69, 0.7)', 'rgba(220, 53, 69, 0.7)'],
                borderColor: ['rgba(40, 167, 69, 1)', 'rgba(220, 53, 69, 1)'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
});
