const addition = require("../tripcostcalculator");
describe("Calculator", () => {
    describe("Addition function", () => {
        test("should return number of days * 1000", () => {
            expect(addition(5)).toBe(1000);
        });
    });
});