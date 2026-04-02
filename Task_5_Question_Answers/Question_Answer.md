1. **You are leading a team of 4 QA engineers. The sprint velocity is dropping due to flaky automation tests. How will you handle this situation?**



**Ans:**



&#x09;First thing i will setup a meeting with the team and discuss, identify which tests are the flaky, troublemakers. So we need to categorise the flakiness. Is it bcoz of the environment, or maybe some synchronization issues like hard coded sleeps. most flaky tests are just waiting for elements to load. So, I will suggest the team use Fluent Waits or Explicit Waits and avoid time.sleep(). 

and also if a test is failing randomly we move it out of the main CI/CD pipeline so it will not block the whole build. We fix it in a separate branch and only when it is stable then we move it back. and also i wiill suggest use Pytest fixtures to make sure each test has its own test data.







2\. **During production release, you find 2 critical bugs reported by the client that were missed in QA. What’s your approach to fix gaps in process and testing?**



**Ans:** 



&#x09;First i will find why we missed them, was if it was a requirement gap or miss during testing. then i update Regression suite if it is miss during testing so i write test cases. then I will check Test coverage like checking Traceability matrix is there any scenario missing or not,if there is gap between user story and tests so it need to discuss with BA or Product owner to fix this.

