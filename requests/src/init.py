import collections
import concurrent.futures
import open_and_load_config
from rest_get import RestTestGet
from rest_post import RestTestPost


def main():
    # load the yaml config
    cfg = open_and_load_config.open_and_load_yaml_file()

    # hostname and headers are common among all tests
    hostname = open_and_load_config.get_host_name(cfg)
    headers = open_and_load_config.get_headers(cfg)

    #TEST
    open_and_load_config.get_includes(cfg)

    # a collection of different tests, with their respective REST urls, etc
    attributes = open_and_load_config.get_test_attributes(cfg)

    # will hold a collection of tests objects containing all their test info and results
    rest_test_get_results = _run_tests(attributes, hostname, headers)

    # list to hold RestAPITestResult objects, which is basically every compare in the config.yml and
    # its test name and url
    list_of_all_results = _assemble_results_with_test_attributes(rest_test_get_results)

    # print results to the console
    _process_results_for_console(list_of_all_results)

def _get_rest_test_objects(hostname, headers, attribute):
    url = open_and_load_config.generate_url(hostname, attribute)
    prep_tests = [_get_rest_test_objects(hostname, headers, attr) for attr in attribute.prep_states]
    verb = attribute.method

    if verb == 'GET':
        return RestTestGet(attribute.name, prep_tests, url, headers, attribute.comparisons)
    elif verb == 'POST':
        return RestTestPost(attribute.name, prep_tests, url, headers, attribute.payload, attribute.comparisons)

def _run_tests(attributes, hostname, headers):
    rest_tests = [_get_rest_test_objects(hostname, headers, attr)
                  for attr in attributes]

    # don't loop anymore run multithread
    #[rest_test.test_web_service() for rest_test in rest_tests]

    # multi thread processing with futures
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_rest_test = {executor.submit(rest_test.test_web_service): rest_test.url for rest_test in rest_tests}
        for future in concurrent.futures.as_completed(future_rest_test):
            #we don't use this data explicitly, it is saved within the object, but can be used for
            #debug, but is needed to block so that we can process the complete list when it is done
            rest_test_result = future_rest_test[future]
            try:
                data = future.result()
            except Exception as exc:
                print('Error testing web service', exc.message)

    # the above loop blocks until we are done, then it runs the following return statement
    return rest_tests

def _assemble_results_with_test_attributes(rest_test_get_results):
    list_of_all_results = list()

    # assembling the results with the tests that they are associated with
    RestAPITestResult = collections.namedtuple('RestAPITestResult', ['name', 'url', 'isPass', 'message'])

    # list of RestTestGet objects
    for rest_test_get in rest_test_get_results:
        # each object's list of validation results
        [list_of_all_results.append(
            [RestAPITestResult(rest_test_get.name, rest_test_get.url, results.isPass, results.message) for results in
             rest_test_get.results][counter]) for counter in range(len(rest_test_get.results))]

    return list_of_all_results


def _process_results_for_console(list_of_all_results):
    # print results to the console
    print('---------------------------- FAILURES ---------------------------------')
    failures = filter(lambda x: x.isPass is False, list_of_all_results)
    for results in failures:
        print(
        'The test we ran is named: {} and the URL is: {} and it passed: {}, the message was: {}'.format(results.name,
                                                                                                        results.url,
                                                                                                        results.isPass,
                                                                                                        results.message))

    print('---------------------------- SUCCESSES ---------------------------------')
    success = filter(lambda x: x.isPass is True, list_of_all_results)
    for results in success:
        print(
        'The test we ran is named: {} and the URL is: {} and it passed: {}, the message was: {}'.format(results.name,
                                                                                                        results.url,
                                                                                                        results.isPass,
                                                                                                        results.message))


if __name__ == '__main__':
    main()
