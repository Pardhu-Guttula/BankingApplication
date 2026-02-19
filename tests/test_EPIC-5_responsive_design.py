import pytest

@pytest.mark.parametrize("device_size, expected_layout", [
    ("small", "single_column"),
    ("medium", "two_columns"),
    ("large", "three_columns")
])
def test_responsive_layout(device_size, expected_layout):
    # Mock function to simulate getting the layout based on device size
    def get_layout_based_on_device_size(size):
        layouts = {
            "small": "single_column",
            "medium": "two_columns",
            "large": "three_columns"
        }
        return layouts[size]

    assert get_layout_based_on_device_size(device_size) == expected_layout
