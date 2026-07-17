import great_expectations as gx


def validate_sensor_data(df):
    """
    Validate transformed sensor data using Great Expectations.
    Returns True if validation succeeds, otherwise False.
    """

    print("\nStarting Data Quality Validation...\n")

    # Create temporary GX context
    context = gx.get_context(mode="ephemeral")

    # Create temporary datasource
    datasource = context.data_sources.add_pandas(
        name="sensor_datasource"
    )

    # Create dataframe asset
    asset = datasource.add_dataframe_asset(
        name="sensor_asset"
    )

    # Batch definition
    batch_definition = asset.add_batch_definition_whole_dataframe(
        "sensor_batch"
    )

    # Create batch
    batch = batch_definition.get_batch(
        batch_parameters={
            "dataframe": df
        }
    )

    # Validator
    validator = context.get_validator(
        batch=batch
    )

    # -----------------------------
    # Expectations
    # -----------------------------

    # Rule 1
    validator.expect_column_values_to_not_be_null(
        "sensor_id"
    )

    # Rule 2
    validator.expect_column_values_to_not_be_null(
        "timestamp"
    )

    # Rule 3
    validator.expect_column_values_to_be_unique(
        "timestamp"
    )

    # Rule 4
    validator.expect_column_values_to_be_between(
        "pressure_psi",
        min_value=0,
        max_value=200,
    )

    # Rule 5
    validator.expect_column_values_to_be_between(
        "temperature",
        min_value=0,
        max_value=100,
    )

    # Execute validation
    results = validator.validate()

    if results.success:
        print("✅ Data Quality Validation PASSED")
        return True

    else:
        print("❌ Data Quality Validation FAILED")
        return False