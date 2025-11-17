# [your_file].py

# Copyright (C) [2025] Eduardo Antonio Ferrera Rodríguez
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY. See the COPYING file for more details.


# pyfront/content.py

class ContentItem:
    """
    Represents a simple content element:
    <tag>text</tag>
    """

    def __init__(self, tag: str, text: str):
        self.tag = tag
        self.text = text

    def render(self, indent: int = 0):
        space = " " * indent
        return f"{space}<{self.tag}>{self.text}</{self.tag}>\n"


class ContentFactory:
    """
    Responsible for creating ContentItem objects from keys like 'ctn_p', 'ctn_h1', etc.
    """

    # Official list of supported tags
    SUPPORTED_TAGS = {
        "p", "span",
        "b", "strong", "i", "u", "em", "small", "mark", "code",
        "h1", "h2", "h3", "h4", "h5", "h6"
    }

    @classmethod
    def is_ctn_key(cls, key: str) -> bool:
        """Checks if the key follows the 'ctn_tag' pattern."""
        return key.startswith("ctn_") and key[4:] in cls.SUPPORTED_TAGS

    @classmethod
    def create_from_kwargs(cls, **kwargs):
        """
        Processes kwargs and returns a list of ContentItem.
        Example: ctn_p="hello" → ContentItem("p", "hello")
        """
        items = []

        for key, value in kwargs.items():
            if cls.is_ctn_key(key):
                tag = key[4:]  # remove 'ctn_'
                items.append(ContentItem(tag, value))

        return items
