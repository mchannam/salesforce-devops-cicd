@IsTest
private class ReferenceHealthCheckTest {
    @IsTest
    static void statusReturnsOk() {
        System.assertEquals('OK', ReferenceHealthCheck.status());
    }
}
