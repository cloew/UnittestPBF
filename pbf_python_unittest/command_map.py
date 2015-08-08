from pbf.Commands.command_manager import CommandConfig, RegisterCommands

commands = [CommandConfig("insert function-test", "pbf_python_unittest.Commands.insert_function_test.InsertFunctionTest", description="Insert a Python Function Test Class in a pre-existing Python test file"),
            CommandConfig("new test", "pbf_python_unittest.Commands.new_test.NewTest", description="Creates a new Python unittest file"),
            CommandConfig("new test-for", "pbf_python_unittest.Commands.new_test_for.NewTestFor", description="Creates a new Python unittest file for the provided file")]

RegisterCommands(commands)